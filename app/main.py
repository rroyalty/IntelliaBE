from app.models import lesson
from typing import List

from fastapi import Depends, FastAPI, APIRouter, Query, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from .models.lesson import Lesson as lessonModel 
from .schemas.lesson import Lesson as lessonSchema
from .models import lesson as pyLesson



from .database.session import SessionLocal, engine
from .database.dependency import get_db

app = FastAPI()
api_router = APIRouter()


pyLesson.Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

@app.get("/")
def main():
    return RedirectResponse(url="/docs/")

@app.get("/lessons/", response_model=List[lessonSchema])
def show_records(db: Session = Depends(get_db)):
    records = db.query(lessonModel).all()
    return records