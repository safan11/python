from pydantic import BaseModel

class Employee(BaseModel):
    id: int
    name: str
    salary: float



class Product(BaseModel):
    id: int
    name: str
    price: float

