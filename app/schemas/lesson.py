from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import date

class Lesson(BaseModel):
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

    class Config:
        orm_mode = True