from sqlalchemy import Boolean, Column, ForeignKey,  String, DateTime, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Time,Date,DateTime,BLOB, JSON,Float
from sqlalchemy.orm import relationship
from datetime import date, datetime
from models import engine
#import bcrypt
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
Base.metadata.bind = engine

class User(Base):

    __tablename__="user"

    id =Column(Integer,autoincrement=True,primary_key=True,index=True)
    Username=Column(String(255),nullable=False)
    Password=Column(String(255),nullable=False)
    
    
    
   

Base.metadata.create_all(bind=engine)