import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = 'mysql+mysqlconnector://hutmjiwus27e4j9t:xd8010ms79n0w4wa@s29oj5odr85rij2o.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/f3373jcbm64lndzf'

# os.getenv("DB_CONN")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

