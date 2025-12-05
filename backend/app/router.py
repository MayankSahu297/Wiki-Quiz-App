from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, HttpUrl
from sqlalchemy.orm import Session
from .database import get_db
from . import models, schemas, scraper, llm

router = APIRouter()

class GenerateRequest(BaseModel):
    url: HttpUrl

@router.post("/generate", response_model=schemas.QuizResponse, status_code=status.HTTP_201_CREATED)
async def generate_quiz(request: GenerateRequest, db: Session = Depends(get_db)):
    import time
    import traceback
    
    try:
        # Check if article already processed
        article = db.query(models.Article).filter(models.Article.url == str(request.url)).first()
        if article:
            # Return latest quiz for this article
            quiz = db.query(models.Quiz).filter(models.Quiz.article_id == article.id).order_by(models.Quiz.generated_at.desc()).first()
            if quiz:
                return schemas.QuizResponse.from_orm(quiz)
        
        # Scrape article
        start_time = time.time()
        try:
            print(f"Scraping {request.url}...")
            scraped = await scraper.scrape_wikipedia(request.url)
            print(f"Scraped in {time.time() - start_time:.2f}s")
        except Exception as e:
            print(f"Scraping failed: {e}")
            traceback.print_exc()
            raise HTTPException(status_code=400, detail=f"Failed to scrape URL: {e}")
        
        # Store article only if it doesn't exist
        if not article:
            article = models.Article(
                url=str(request.url),
                title=scraped.title,
                summary=scraped.summary,
                raw_html=scraped.raw_html,
            )
            db.add(article)
            db.commit()
            db.refresh(article)
        
        # Generate quiz via LLM
        gen_start = time.time()
        print("Generating quiz...")
        try:
            quiz_data = await llm.generate_quiz(scraped)
            print(f"Generated in {time.time() - gen_start:.2f}s")
        except Exception as e:
            print(f"Quiz generation failed: {e}")
            traceback.print_exc()
            raise HTTPException(status_code=500, detail=f"Failed to generate quiz: {e}")
        
        # Store quiz JSON
        quiz = models.Quiz(article_id=article.id, data=quiz_data)
        db.add(quiz)
        db.commit()
        db.refresh(quiz)
        return schemas.QuizResponse.from_orm(quiz)
    except HTTPException:
        raise
    except Exception as e:
        print(f"Unexpected error in generate_quiz: {e}")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@router.get("/history", response_model=list[schemas.ArticleSummary])
def get_history(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    articles = db.query(models.Article).order_by(models.Article.created_at.desc()).offset(skip).limit(limit).all()
    return [schemas.ArticleSummary.from_orm(a) for a in articles]

@router.get("/quiz/{quiz_id}", response_model=schemas.QuizResponse)
def get_quiz(quiz_id: int, db: Session = Depends(get_db)):
    quiz = db.query(models.Quiz).filter(models.Quiz.id == quiz_id).first()
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")
    return schemas.QuizResponse.from_orm(quiz)
