from pydantic import BaseModel, HttpUrl
from typing import Optional, Sequence
from datetime import date

class LessonBase(BaseModel):
    department: str
    course: str
    subject: str
    name: str
    description: Optional[str] = None
    tier: str #Elementary, Middle, High
    grade: int #K-12
    materials: list
    instructions: dict
    created_by: str
    created_on: date
    url: HttpUrl

class LessonCreate(LessonBase):
    department: str
    course: str
    subject: str
    name: str
    description: Optional[str] = None
    tier: str #Elementary, Middle, High
    grade: int #K-12
    materials: list
    instructions: dict
    created_by: str
    created_on: date
    url: HttpUrl

class LessonUpdate(LessonBase):
    name: str
    description: Optional[str] = None
    tier: str #Elementary, Middle, High
    grade: int #K-12
    materials: list
    instructions: dict

class LessonInDBBase(LessonBase):
    id: int

    class Config:
        orm_mode = True

class Lesson(LessonInDBBase):
    pass

class LessonInDB(LessonInDBBase):
    pass

class LessonSearchResults(BaseModel):
    results: Sequence[Lesson]