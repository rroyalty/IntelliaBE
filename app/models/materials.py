from sqlalchemy import Column, Integer, String
from ..database.session import Base

class Materials(Base):
    __tablename__ = "Lessons"

    id = Column(Integer, primary_key=True, nullable=False)
    material = Column(String(30), nullable=False)

    #index=True, autoincrement=True,