from pydantic import BaseModel

class Lessons(BaseModel):
    id: int
    department: str
    course: str
    subject: str

    class Config:
        orm_mode = True