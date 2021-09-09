import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'mysql+mysqlconnector://root:youcannotpassword@127.0.0.1?statusColor=&enviroment=local&name=&tLSMode=0&usePrivateKey=false&safeModeLevel=0&advancedSafeModeLevel=0'

# os.getenv("DB_CONN")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()