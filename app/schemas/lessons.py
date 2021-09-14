from pydantic import BaseModel, HttpUrl
from typing import Optional, List
from datetime import date


class Lessons(BaseModel):
    id: int
    department: str
    course: str
    subject: str
    name: str
    description: Optional[str] = None
    tier: str #Elementary, Middle, High
    grade: int #K-12
    created_by: str
    # created_on: date
    # url: HttpUrl

    class Config:
        orm_mode = True