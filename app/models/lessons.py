
from sqlalchemy import Column, Integer, String, PickleType, Date
from sqlalchemy.sql.sqltypes import JSON
from ..database import Base
from sqlalchemy.ext.mutable import MutableList
from datetime import date
import os

class Lessons(Base):
    __tablename__ = "Lessons"

    id = Column(Integer, primary_key=True, index=True)
    department = Column(String(30), nullable=False)
    course = Column(String(30), nullable=False)
    subject = Column(String(30), nullable=False)
    name = Column(String(30), nullable=False)
    description = Column(String(255))
    materials = Column(MutableList.as_mutable(PickleType), default=[])
    instructions = Column(JSON)
    tier = Column(String(20), nullable=False) #Elementary, Middle, High
    grade = Column(String(2), nullable=False) #K-12
    created_by = Column(String(30), default=os.environ["USER"])
    created_on = Column(Date, default=date.today())

    # def __init__(self, created_on, created_by, id) -> None:
    #     self.created_on = created_on
    #     self.created_by = created_by
    #     self.id = id
