# Import FastAPI to create our application
from fastapi import FastAPI

# Import database objects used to create the tables
from app.database.connection import Base, engine

# Import Employee model so SQLAlchemy knows about the table
from app.models.employee import Employee

# Import our Employee API router
from app.routers.employee_router import router as employee_router


# Create the employees table if it does not already exist
Base.metadata.create_all(bind=engine)


# Create the FastAPI application
app = FastAPI(
    title="Employee CRUD API"
)


# Register all Employee APIs with the FastAPI application
app.include_router(employee_router)


# Simple test endpoint
@app.get("/")
def home():

    return {
        "message": "Employee CRUD API is running"
    }