from pydantic import BaseModel
from typing import Optional

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
    # url: HttpUrl

    class Config:
        orm_mode = True