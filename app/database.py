import os

from sqlalchemy import create_engine  # type: ignore
from sqlalchemy.ext.declarative import declarative_base  # type: ignore
from sqlalchemy.orm import sessionmaker  # type: ignore

os.environ["POSTGRES_HOST"] = "ec2-44-198-223-154.compute-1.amazonaws.com"
os.environ["POSTGRES_DB"] = "d5rj3ncvb47hfb"
os.environ["POSTGRES_USER"] = "ahpxpxlvkbdeoa"
os.environ["POSTGRES_PASS"] = "aa545069c2e4376f0aa11f9bdb88b51b9c3ee4419ad27e9ffba2c2639ad8453c"
os.environ["POSTGRES_PORT"] = "5432"

host = os.environ["POSTGRES_HOST"]
port = os.environ["POSTGRES_PORT"]
user = os.environ["POSTGRES_USER"]
password = os.environ["POSTGRES_PASS"]
db = os.environ["POSTGRES_DB"]
dbtype = "postgresql"

SQLALCHEMY_DATABASE_URI = f"{dbtype}://{user}:{password }@{host}:{port}/{db}"

engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()