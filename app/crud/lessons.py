from typing import List

from sqlalchemy.orm import Session  # type: ignore

from ..models.lessons import Lessons

def get_lesson_by_name(session: Session, name: str) -> Lessons:
    return session.query(Lessons).filter(Lessons.name == name).first()

def get_lessons(session: Session) -> List[Lessons]:
    return session.query(Lessons).all()