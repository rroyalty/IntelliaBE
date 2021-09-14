from pydantic import BaseModel, HttpUrl
from typing import Optional, List
from datetime import date


class Materials(BaseModel):
    id: int
    materials: str

    class Config:
        orm_mode = True