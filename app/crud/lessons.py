from typing import List, TypeVar

from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from ..models.lessons import Lessons, Base
from ..schemas.lessons import BaseModel

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

def get_lesson_by_name(session: Session, name: str) -> ModelType:
    return session.query(Lessons).filter(Lessons.name == name).first()

def get_lesson_by_id(session: Session, id: int) -> ModelType:
    return session.query(Lessons).filter(Lessons.id == id).first()

def get_lessons(session: Session) -> List[ModelType]:
    return session.query(Lessons).all()

def add_lesson(obj_in: UpdateSchemaType, session: Session) -> ModelType:
    obj_in_data = jsonable_encoder(obj_in)
    obj_db = Lessons(**obj_in_data)
    session.add(obj_db)
    session.commit()
    session.refresh(obj_db)
    return obj_db

def update_lesson(id: int, obj_in: UpdateSchemaType, session: Session) -> ModelType:
    obj_in_data = jsonable_encoder(obj_in)
    obj_db = Lessons(**obj_in_data)
    obj_old = get_lesson_by_id(session, id)
    if obj_old is None:
        return None
    for key, value in vars(obj_old).items():
        setattr(obj_db, key, value) if value else None
    session.add(obj_db)
    session.commit()
    session.refresh(obj_db)
    return obj_db

def remove_lesson(id: int, session: Session) -> ModelType:
    session.query(Lessons).filter(Lessons.id==id).delete()
    session.commit()
