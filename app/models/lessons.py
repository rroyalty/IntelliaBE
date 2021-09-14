from sqlalchemy import Column, Integer, String
from ..database.session import Base

class Lessons(Base):
    __tablename__ = "Lessons"

    id = Column(Integer, primary_key=True, nullable=False)
    department = Column(String(30), nullable=False)
    course = Column(String(30), nullable=False)
    subject = Column(String(30), nullable=False)
    name = Column(String(30), nullable=False)
    description = Column(String(255))
    tier = Column(String(10), nullable=False) #Elementary, Middle, High
    grade = Column(String(2), nullable=False) #K-12
    created_by = Column(String(30), nullable=False)
