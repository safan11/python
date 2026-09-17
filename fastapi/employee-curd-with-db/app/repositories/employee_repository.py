# Session is used to communicate with the database
from sqlalchemy.orm import Session

# Import our SQLAlchemy Employee model
from app.models.employee import Employee


# CREATE: Add a new employee to the database
def create_employee(db: Session, employee: Employee):

    db.add(employee)
    db.commit()
    db.refresh(employee)

    return employee


# READ: Get all employees from the database
def get_all_employees(db: Session):

    return db.query(Employee).all()


# READ: Get one employee using its ID
def get_employee_by_id(db: Session, employee_id: int):

    return db.query(Employee).filter(
        Employee.id == employee_id
    ).first()


# UPDATE: Change an existing employee's details
def update_employee(
    db: Session,
    employee: Employee,
    name: str,
    email: str,
    department: str,
    salary: float
):

    employee.name = name
    employee.email = email
    employee.department = department
    employee.salary = salary

    db.commit()
    db.refresh(employee)

    return employee


# DELETE: Remove an employee from the database
def delete_employee(db: Session, employee: Employee):

    db.delete(employee)
    db.commit()

    return True