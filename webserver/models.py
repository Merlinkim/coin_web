from sqlalchemy import Column,Integer,String,Text,DateTime,ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class UserCreate(Base):
    __tablename= "user"

    id = Column(Integer,primary_key=True)
    username = Column(String,nullable=False)
    password = Column(String,nullable=False)
    email = Column(String,nullable=False)
    