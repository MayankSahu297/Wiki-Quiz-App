import asyncio
import httpx
from bs4 import BeautifulSoup
from pydantic import HttpUrl
from typing import NamedTuple

class ScrapedArticle(NamedTuple):
    title: str
    summary: str
    raw_html: str
    sections: list[str]
    text: str

async def fetch_html(url: HttpUrl) -> str:
    headers = {
        "User-Agent": "WikiQuizApp/1.0 (mailto:your-email@example.com) python-httpx/0.23.0"
    }
    async with httpx.AsyncClient(timeout=20.0, headers=headers, follow_redirects=True) as client:
        resp = await client.get(str(url))
        resp.raise_for_status()
        return resp.text

async def scrape_wikipedia(url: HttpUrl) -> ScrapedArticle:
    html = await fetch_html(url)
    soup = BeautifulSoup(html, "html.parser")
    
    # Title
    title_tag = soup.find("h1", {"id": "firstHeading"})
    title = title_tag.get_text(strip=True) if title_tag else ""
    
    content_div = soup.find("div", {"class": "mw-parser-output"})
    summary = ""
    sections = []
    text_content = ""

    if content_div:
        # Summary: First non-empty paragraph
        for p in content_div.find_all("p", recursive=False):
            txt = p.get_text(strip=True)
            if txt:
                summary = txt
                break
        
        # Sections: h2 headings
        for h2 in content_div.find_all("h2"):
            span = h2.find("span", {"class": "mw-headline"})
            if span:
                sections.append(span.get_text(strip=True))
        
        # Full Text: All paragraphs joined
        paragraphs = [p.get_text(strip=True) for p in content_div.find_all("p")]
        text_content = "\n".join(p for p in paragraphs if p)
        text_content = text_content[:6000]  # Limit to 6000 chars for LLM context

    return ScrapedArticle(title=title, summary=summary, raw_html=html, sections=sections, text=text_content)
