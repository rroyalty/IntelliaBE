from typing import List

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from .models.lesson import Base, Lesson
from .schemas.lesson import Lesson
from .database.database import SessionLocal, engine


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# Dependency
def get_db():
    try:
        db = SessionLocal()
        print(db)
        yield db
    finally:
        db.close()

@app.get("/")
async def main():
    return RedirectResponse(url="/docs/")


@app.get("/lessons/", response_model=List[Lesson])
async def show_records(db: Session = Depends(get_db)):
    records = db.query(Lesson).all()
    return records