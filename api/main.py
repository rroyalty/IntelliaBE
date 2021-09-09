from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

class Lesson(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    tier: str #Elementary, Middle, High
    grade: int #K-12
    created_by: str
    created_on: str
    


app = FastAPI()

@app.get("/lessons")
async def get_lessons():
        return {"Lessons" : "All"}

@app.get("/lessons/{lesson_id}")
async def get_lesson_by_id(lesson_id: Lesson):
        return {"Lesson" : lesson_id}

@app.put("/lessons/{lesson_id}")
async def put_lesson_by_id(lesson_id: Lesson):
        return {"Lesson" : lesson_id}

@app.post("/lessons/{lesson_id}")
async def post_lesson_by_id(lesson_id: Lesson):
        return {"Lesson" : lesson_id}

@app.delete("/lessons/{lesson_id}")
async def delete_lesson_by_id(lesson_id: Lesson):
        return {"Lesson" : lesson_id}