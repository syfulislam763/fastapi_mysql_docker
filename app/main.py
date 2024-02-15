from sqlalchemy import Column, Integer, String
from fastapi import FastAPI, Depends
from .database import SessionLocal, Base, engine
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import List

class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    email = Column(String(30), unique=True)


class PersonSchema(BaseModel):
    id:int
    name:str
    email:str

    class Config:
        from_attributes=True
class PersonResSchema(BaseModel):
    persons: List[PersonSchema]

    class Config:
        from_attributes=True

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"msg":"Hello World"}


@app.post("/api/person", response_model=PersonSchema)
def create_person(payload:PersonSchema, db:Session = Depends(get_db)):
    person = Person(id = payload.id, name=payload.name, email=payload.email)
    db.add(person)
    db.commit()
    db.refresh(person)
    return person

@app.get("/api/person", response_model=PersonResSchema)
def get_person(db:Session=Depends(get_db)):
    return {"persons": db.query(Person).all()}
    
