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
async def post_lesson(db_objid, db_objdepartment, db_objcourse, db_objsubject, db_objname, db_objdescription, db_objtier, db_objgrade, db_objmaterials, db_objinstructions, db_objcreated_by, db_objcreated_on, db: Session = Depends(get_db)):
    db.add(lessonModel(
        id=db_objid,
        department=db_objdepartment,
        course=db_objcourse,
        subject=db_objsubject,
        name=db_objname,
        description=db_objdescription,
        tier=db_objtier,
        grade=db_objgrade,
        materials=db_objmaterials,
        instructions=db_objinstructions,
        created_by=db_objcreated_by,
        # created_on=db_objcreated_on
        )
    )
    db.commit()

