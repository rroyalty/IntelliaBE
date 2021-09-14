from pydantic import BaseModel

class Materials(BaseModel):
    id: int
    material: str

    class Config:
        orm_mode = True