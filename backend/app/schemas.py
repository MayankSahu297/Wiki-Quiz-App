from pydantic import BaseModel, HttpUrl, Field, ConfigDict
from typing import List, Dict, Any, Optional
from datetime import datetime

class ArticleSummary(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    url: str  # Changed from HttpUrl to str for compatibility
    title: str
    created_at: Optional[datetime] = None

class QuizResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    url: Optional[str] = None
    title: str
    summary: str
    key_entities: Optional[Dict[str, List[str]]] = None
    sections: Optional[List[str]] = None
    quiz: Optional[List[Dict[str, Any]]] = None
    related_topics: Optional[List[str]] = None

    @classmethod
    def from_orm(cls, quiz_obj):
        # quiz_obj.data holds the full JSON payload as stored
        data = quiz_obj.data
        # Add article URL and ID
        return cls(
            id=quiz_obj.id,
            url=quiz_obj.article.url,
            title=data.get('title', quiz_obj.article.title),
            summary=data.get('summary', quiz_obj.article.summary),
            key_entities=data.get('key_entities'),
            sections=data.get('sections'),
            quiz=data.get('quiz', []),
            related_topics=data.get('related_topics')
        )
