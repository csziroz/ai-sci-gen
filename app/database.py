# Логика подключения к базе данных

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import Scientist

DATABASE_URL = "sqlite:///./ai_sci_gen.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def init_db():
    Base.metadata.create_all(bind=engine)

def create_record(input_data, biography, image_url):
    session = SessionLocal()
    new_record = Scientist(
        gender=input_data.gender,
        age=input_data.age,
        field=input_data.field,
        personality=input_data.personality,
        appearance=input_data.appearance,
        biography=biography,
        image_url=image_url,
    )
    session.add(new_record)
    session.commit()
    session.refresh(new_record)
    return new_record.id

def get_record(record_id):
    session = SessionLocal()
    return session.query(Scientist).filter(Scientist.id == record_id).first()
