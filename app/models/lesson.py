from sqlalchemy import Column, Integer, String, PickleType
from sqlalchemy.types import Date


from . import Base

class Lesson(Base):
    __tablename__ = "Lessons"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    department = Column(String(30), nullable=False)
    course = Column(String(30), nullable=False)
    subject = Column(String(30), nullable=False)
    name = Column(String(30), nullable=False)
    description = Column(String(255))
    tier = Column(String(10), nullable=False) #Elementary, Middle, High
    grade = Column(String(2), nullable=False) #K-12
    materials = Column(PickleType)
    instructions = Column(PickleType)
    created_by = Column(String(30), nullable=False)
    created_on = Column(Date, nullable=False)