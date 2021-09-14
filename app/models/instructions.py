from sqlalchemy import Column, Integer, String
from ..database.session import Base

class Instructions(Base):
    __tablename__ = "Lessons"

    id = Column(Integer, primary_key=True, nullable=False)
    step = Column(Integer, nullable=False)
    instructon = Column(String(500), nullable=False)
    timeEst = Column(Integer, nullable=False)