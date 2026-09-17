# SQLAlchemy functions for connecting to MySQL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# MySQL connection details
DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/employee_db"


# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)


# Create database sessions using our MySQL engine
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Base class for all SQLAlchemy models
Base = declarative_base()


# Creates a database session for each API request
def get_db():

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()