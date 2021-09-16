from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session  # type: ignore
from pydantic import BaseModel

from ..crud import lessons as crud
from ..models import lessons as model
from ..database import SessionLocal, engine
from ..schemas.lessons import Lessons as schema

model.Base.metadata.create_all(bind=engine)
router = APIRouter()

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@router.get("/lessons/", response_model=List[schema])
def read_lessons(
   session: Session = Depends(get_session)
):
    lessons = crud.get_lessons(session=session)
    return lessons


@router.get("/lessons/{name}", response_model=schema)
def read_lesson(name: str, session: Session = Depends(get_session)):
    lesson = crud.get_lesson_by_name(session=session, name=name)
    if lesson is None:
        raise HTTPException(status_code=404, detail="lesson not found")
    return lesson

@router.post("/lessons", response_model=schema)
def new_lesson(*, obj_in: schema, session: Session = Depends(get_session)):
    session.expunge_all
    lesson = crud.add_lesson(session=session, obj_in=obj_in)
    return lesson