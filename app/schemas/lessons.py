from pydantic import BaseModel
from typing import Optional, List, Dict

class Instruction(BaseModel):
    id: int
    step: int
    instruction: str
    timeEst: int

    class Config:
        orm_mode = True

class Lessons(BaseModel):
    id: int
    department: str
    course: str
    subject: str
    name: str
    description: Optional[str] = None
    tier: str #Elementary, Middle, High
    grade: int #K-12
    instructions: List[Instruction]
    created_by: str
    # url: HttpUrl

    class Config:
        orm_mode = True