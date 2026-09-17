# BaseModel validates the data received from the API
from pydantic import BaseModel


# Defines the data required when creating or updating an employee
class EmployeeCreate(BaseModel):

    name: str
    email: str
    department: str
    salary: float


# Defines the data that our API will send back to the client
class EmployeeResponse(BaseModel):

    id: int
    name: str
    email: str
    department: str
    salary: float

    # Allows Pydantic to convert SQLAlchemy objects into JSON responses
    class Config:
        from_attributes = True