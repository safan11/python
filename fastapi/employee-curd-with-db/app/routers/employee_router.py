# FastAPI classes used to create routes and handle errors
from fastapi import APIRouter, Depends, HTTPException

# Session represents our SQLAlchemy database session
from sqlalchemy.orm import Session

# get_db creates a database session for each request
from app.database.connection import get_db

# Schemas validate input and define the API response
from app.schemas.employee import EmployeeCreate, EmployeeResponse

# Service contains our employee business logic
from app.services import employee_service


# Create a router for all employee-related APIs
router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


# CREATE: POST /employees
@router.post("", response_model=EmployeeResponse)
def create_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):

    return employee_service.create_employee(db, employee)


# READ: GET /employees
@router.get("", response_model=list[EmployeeResponse])
def get_all_employees(
    db: Session = Depends(get_db)
):

    return employee_service.get_all_employees(db)


# READ: GET /employees/{employee_id}
@router.get("/{employee_id}", response_model=EmployeeResponse)
def get_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):

    employee = employee_service.get_employee_by_id(
        db, employee_id
    )

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee


# UPDATE: PUT /employees/{employee_id}
@router.put("/{employee_id}", response_model=EmployeeResponse)
def update_employee(
    employee_id: int,
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):

    updated_employee = employee_service.update_employee(
        db,
        employee_id,
        employee
    )

    if updated_employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return updated_employee


# DELETE: DELETE /employees/{employee_id}
@router.delete("/{employee_id}")
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):

    result = employee_service.delete_employee(
        db, employee_id
    )

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return {
        "message": "Employee deleted successfully"
    }