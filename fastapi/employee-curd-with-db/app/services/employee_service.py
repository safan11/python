# Session allows us to work with the database
from sqlalchemy.orm import Session

# Employee is our SQLAlchemy database model
from app.models.employee import Employee

# EmployeeCreate contains and validates API input data
from app.schemas.employee import EmployeeCreate

# Repository contains all database operations
from app.repositories import employee_repository


# CREATE: Convert schema data into an Employee object and save it
def create_employee(db: Session, employee_data: EmployeeCreate):

    employee = Employee(
        name=employee_data.name,
        email=employee_data.email,
        department=employee_data.department,
        salary=employee_data.salary
    )

    return employee_repository.create_employee(db, employee)


# READ: Get all employees through the repository
def get_all_employees(db: Session):

    return employee_repository.get_all_employees(db)


# READ: Get one employee by ID
def get_employee_by_id(db: Session, employee_id: int):

    return employee_repository.get_employee_by_id(db, employee_id)


# UPDATE: Find the employee first, then update its details
def update_employee(
    db: Session,
    employee_id: int,
    employee_data: EmployeeCreate
):

    employee = employee_repository.get_employee_by_id(
        db, employee_id
    )

    if employee is None:
        return None

    return employee_repository.update_employee(
        db,
        employee,
        employee_data.name,
        employee_data.email,
        employee_data.department,
        employee_data.salary
    )


# DELETE: Find the employee first, then remove it
def delete_employee(db: Session, employee_id: int):

    employee = employee_repository.get_employee_by_id(
        db, employee_id
    )

    if employee is None:
        return False

    return employee_repository.delete_employee(db, employee)