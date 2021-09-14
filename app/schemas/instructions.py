from pydantic import BaseModel, HttpUrl
from typing import Optional, List
from datetime import date


class Lessons(BaseModel):
    id: int
    department: str
    course: str
    subject: str

    class Config:
        orm_mode = True