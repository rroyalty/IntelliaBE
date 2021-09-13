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
async def get_all_lessons(db: Session = Depends(get_db)):
    lessons = db.query(lessonModel).all()
    return lessons

@app.get("/lessons/{id}", response_model=List[lessonSchema])
async def get_lesson_by_id(id: int, db: Session = Depends(get_db)):
    lesson = db.query(lessonModel).filter(lessonModel.id == id).first()
    return lesson

@app.post("/lessons/", response_model=List[lessonSchema])
async def post_lesson(postId: int, postDepartment: str, postCourse: str, db: Session = Depends(get_db)):
    db.add(lessonModel(
        id=postId,
        department=postDepartment,
        course=postCourse
        )
    )
    db.commit()

