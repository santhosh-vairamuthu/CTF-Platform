from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from models import engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
Base.metadata.bind = engine

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    Username = Column(String(255), nullable=False)
    Password = Column(String(255), nullable=False)

class Score(Base):
    __tablename__ = "score"
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    Username = Column(String(255), nullable=False)
    problem_id = Column(String(20), nullable=False)
    score = Column(Integer, nullable=False)
    submitted_at = Column(DateTime, default=datetime.now) 

Base.metadata.create_all(bind=engine)
