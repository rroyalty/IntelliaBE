from sqlalchemy import Column, Integer, String, PickleType
from sqlalchemy.types import Date

from .database import Base

class Lesson(Base):
    __tablename__ = "Lessons"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullible=False)
    department = Column(String(30), nullible=False)
    course = Column(String(30), nullible=False)
    subject = Column(String(30), nullible=False)
    name = Column(String(30), nullible=False)
    description = Column(String(255), Optional=True)
    tier = Column(String(10), nullible=False) #Elementary, Middle, High
    grade = Column(String(2), nullible=False) #K-12
    materials = Column(PickleType, Optional = True)
    instructions = Column(PickleType)
    created_by = Column(String(30), nullible=False)
    created_on = Column(Date, nullible=False)