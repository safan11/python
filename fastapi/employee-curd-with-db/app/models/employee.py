# Import SQLAlchemy column types.
#
# Column  -> defines a database column
# Integer -> stores whole numbers
# String  -> stores text
# Float   -> stores decimal numbers
from sqlalchemy import Column, Integer, String, Float


# Import Base from our database connection.
# Employee will inherit from Base, which tells SQLAlchemy
# that Employee is a database model.
from app.database.connection import Base


# Employee model.
# This class represents the "employees" table in MySQL.
class Employee(Base):

    # Name of the table in MySQL.
    __tablename__ = "employees"


    # Employee ID.
    #
    # Integer      -> number
    # primary_key  -> unique identifier
    # index=True   -> creates an index for faster searching
    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    # Employee name.
    #
    # String(100)  -> maximum 100 characters
    # nullable=False -> value is required
    name = Column(
        String(100),
        nullable=False
    )


    # Employee email.
    #
    # String(150)  -> maximum 150 characters
    # unique=True  -> duplicate emails are not allowed
    # nullable=False -> email is required
    email = Column(
        String(150),
        unique=True,
        nullable=False
    )


    # Employee department.
    #
    # String(100) -> maximum 100 characters
    # nullable=False -> department is required
    department = Column(
        String(100),
        nullable=False
    )


    # Employee salary.
    #
    # Float -> allows values such as:
    # 50000
    # 55000.50
    salary = Column(
        Float,
        nullable=False
    )