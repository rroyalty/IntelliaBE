from typing import List

from fastapi import Depends, FastAPI, APIRouter, Query, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from .database.base_class import Base
from .schemas.lesson import Lesson
from .database.session import SessionLocal, engine

from app import crud

Base.metadata.create_all(bind=engine)

app = FastAPI()
api_router = APIRouter()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@api_router.get("/lessons/", status_code=200)
def lessons(
    request: Request,
    db: Session = Depends(get_db),
) -> dict:
    """
    Root GET
    """
    lessons = crud.recipe.get_multi(db=db, limit=10)
    return lessons



# @api_router.get("/lessons/", response_model=List[Lesson])
# async def show_records(db: Session = Depends(get_db)):
#     records = db.query(Lesson).all()
#     return records