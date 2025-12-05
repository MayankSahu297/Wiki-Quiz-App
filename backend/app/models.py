from sqlalchemy import Column, Integer, String, Text, JSON, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base
import datetime

class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, unique=True, nullable=False)
    title = Column(String, nullable=False)
    summary = Column(Text)
    raw_html = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    # relationship to quizzes
    quizzes = relationship("Quiz", back_populates="article")

class Quiz(Base):
    __tablename__ = "quizzes"
    id = Column(Integer, primary_key=True, index=True)
    article_id = Column(Integer, ForeignKey("articles.id"), nullable=False)
    generated_at = Column(DateTime, default=datetime.datetime.utcnow)
    data = Column(JSON)  # stores full JSON output (quiz, related topics, etc.)
    article = relationship("Article", back_populates="quizzes")
