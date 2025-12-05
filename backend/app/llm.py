import os
import json
from typing import Dict, Any
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import HttpUrl
from .scraper import ScrapedArticle

# Load Gemini API key from environment (set in .env)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
USE_MOCK = os.getenv("USE_MOCK_LLM", "false").lower() == "true"

if not GEMINI_API_KEY and not USE_MOCK:
    raise RuntimeError("GEMINI_API_KEY not set in environment variables")

# Initialize LLM (using flash model for cost‑efficiency)
if not USE_MOCK:
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", temperature=0.7, api_key=GEMINI_API_KEY)

# Prompt template – ask LLM to return JSON matching our expected schema
PROMPT_TEMPLATE = """
You are an expert quiz generator. Given the text of a Wikipedia article, produce a JSON object with the following fields:
- title: article title (string)
- summary: a concise 2-3 sentence summary (string)
- key_entities: an object with three arrays:
    * people: list of important people mentioned (max 5)
    * organizations: list of organizations/companies mentioned (max 5)
    * locations: list of places/locations mentioned (max 5)
- sections: list of main section titles from the article (max 8)
- quiz: an array of 5-10 questions. Each question must contain:
    * question (string)
    * options (list of four strings labelled A-D)
    * correct_answer (the correct option string, e.g. "A) Option Text")
    * difficulty (one of "easy", "medium", "hard")
    * explanation (short sentence why this is correct)
- related_topics: list of 3-5 related Wikipedia topics the user might want to explore

Only output raw JSON (no markdown, no extra text). Use the following data:
Title: {title}
Summary: {summary}
Text Content:
{text}
"""

def generate_mock_quiz(scraped: ScrapedArticle) -> Dict[str, Any]:
    """Generate a mock quiz for testing when API quota is exceeded."""
    return {
        "title": scraped.title,
        "summary": scraped.summary[:200] + "..." if len(scraped.summary) > 200 else scraped.summary,
        "key_entities": {
            "people": ["Notable Person 1", "Notable Person 2", "Expert Researcher"],
            "organizations": ["Wikipedia Foundation", "Research Institute"],
            "locations": ["United States", "Europe", "Global"]
        },
        "sections": [
            "Introduction",
            "History",
            "Key Concepts",
            "Applications",
            "Criticism",
            "See Also"
        ],
        "quiz": [
            {
                "question": f"What is the main topic of this article about {scraped.title}?",
                "options": [
                    f"A) {scraped.title}",
                    "B) Something else",
                    "C) Another topic",
                    "D) None of the above"
                ],
                "correct_answer": f"A) {scraped.title}",
                "difficulty": "easy",
                "explanation": "This is the main subject of the article."
            },
            {
                "question": "According to the article, which statement is most accurate?",
                "options": [
                    "A) The topic is widely studied",
                    "B) The topic is rarely discussed",
                    "C) The topic doesn't exist",
                    "D) The topic is fictional"
                ],
                "correct_answer": "A) The topic is widely studied",
                "difficulty": "medium",
                "explanation": "Based on the comprehensive Wikipedia article."
            },
            {
                "question": f"What can you learn from reading about {scraped.title}?",
                "options": [
                    "A) Historical context and facts",
                    "B) Cooking recipes",
                    "C) Weather patterns",
                    "D) Sports scores"
                ],
                "correct_answer": "A) Historical context and facts",
                "difficulty": "easy",
                "explanation": "Wikipedia articles provide factual information."
            },
            {
                "question": "Which difficulty level best describes this question?",
                "options": [
                    "A) Easy - Basic knowledge",
                    "B) Medium - Moderate understanding",
                    "C) Hard - Expert level",
                    "D) Impossible"
                ],
                "correct_answer": "B) Medium - Moderate understanding",
                "difficulty": "medium",
                "explanation": "This tests your understanding of difficulty levels."
            },
            {
                "question": f"What is a key characteristic of {scraped.title}?",
                "options": [
                    "A) It has historical significance",
                    "B) It's completely unknown",
                    "C) It's purely fictional",
                    "D) It has no documentation"
                ],
                "correct_answer": "A) It has historical significance",
                "difficulty": "hard",
                "explanation": "Most Wikipedia topics have historical or cultural significance."
            }
        ],
        "related_topics": [
            "Related Topic 1",
            "Related Topic 2",
            "Further Reading",
            "See Also"
        ]
    }

async def generate_quiz(scraped: ScrapedArticle) -> Dict[str, Any]:
    """Generate quiz JSON using Gemini via LangChain.
    Returns a dict that can be stored directly in the Quiz model's JSON column.
    """
    # Use mock if enabled
    if USE_MOCK:
        print("Using MOCK quiz generation (USE_MOCK=true)")
        return generate_mock_quiz(scraped)
    
    try:
        prompt = PROMPT_TEMPLATE.format(
            title=scraped.title.replace("{", "{{").replace("}", "}}"),
            summary=scraped.summary.replace("{", "{{").replace("}", "}}"),
            text=scraped.text.replace("{", "{{").replace("}", "}}")  # Escape braces to avoid format errors
        )
        # Call LLM
        response = await llm.ainvoke(prompt)
        
        content = response.content
        print(f"LLM Response: {content[:500]}...") # Log first 500 chars

        # Clean up markdown code blocks if present
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0].strip()
        elif "```" in content:
            content = content.split("```")[0].strip()

        # Parse JSON
        try:
            data = json.loads(content)
            return data
        except Exception as e:
            print(f"JSON Parse Error: {e}")
            print(f"Failed Content: {content}")
            # Fallback to mock on parse error
            print("Falling back to MOCK quiz generation due to parse error")
            return generate_mock_quiz(scraped)
    
    except Exception as e:
        # Catch API quota errors and other exceptions
        error_str = str(e)
        if "429" in error_str or "quota" in error_str.lower():
            print(f"API Quota exceeded: {e}")
            print("Falling back to MOCK quiz generation")
            return generate_mock_quiz(scraped)
        else:
            print(f"LLM Error: {e}")
            print("Falling back to MOCK quiz generation")
            return generate_mock_quiz(scraped)
