from datetime import date
from pydantic import BaseModel
from typing import Optional, List, Dict
import os

class Instruction(BaseModel):
    step: int
    instruction: str
    timeEst: int

    class Config:
        orm_mode = True

class LessonsPost(BaseModel):
    department: str
    course: str
    subject: str
    name: str
    description: Optional[str] = None
    materials: Optional[List[str]] = None
    instructions: List[Instruction]
    tier: str #Elementary, Middle, High
    grade: int #K-12

    class Config:
        orm_mode = True

class LessonsReturn(LessonsPost):
    id: int
    created_by: str
    created_on: date

    class Config:
        orm_mode = True