# SQLAlchemy модели базы данных
from sqlalchemy import Column, Integer, String, Text
from database import Base

class Scientist(Base):
    __tablename__ = 'scientists'
    id = Column(Integer, primary_key=True, index=True)
    gender = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    field = Column(String, nullable=False)
    personality = Column(String, nullable=False)
    appearance = Column(String, nullable=False)
    biography = Column(Text, nullable=False)
    image_url = Column(String, nullable=False)
