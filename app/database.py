import os

from sqlalchemy import create_engine  # type: ignore
from sqlalchemy.ext.declarative import declarative_base  # type: ignore
from sqlalchemy.orm import sessionmaker  # type: ignore

os.environ["POSTGRES_HOST"] = "ec2-54-146-84-101.compute-1.amazonaws.com"
os.environ["POSTGRES_DB"] = "d6qp1n2fdjbo71"
os.environ["POSTGRES_USER"] = "thgzuzfkyqvkhv"
os.environ["POSTGRES_PASS"] = "450b2da429a5544b600e7c780ddb0b40b331baab74927e65fdfc65b8520ac9b5"
os.environ["POSTGRES_PORT"] = "5432"

host = os.environ["POSTGRES_HOST"]
port = os.environ["POSTGRES_PORT"]
user = os.environ["POSTGRES_USER"]
password = os.environ["POSTGRES_PASS"]
db = os.environ["POSTGRES_DB"]
dbtype = "postgresql"


#SQLALCHEMY_DATABASE_URI = f"{dbtype}://{user}:{password }@{host}:{port}/{db}"
SQLALCHEMY_DATABASE_URI = "postgresql://thgzuzfkyqvkhv:450b2da429a5544b600e7c780ddb0b40b331baab74927e65fdfc65b8520ac9b5@ec2-54-146-84-101.compute-1.amazonaws.com:5432/d6qp1n2fdjbo71"

engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()