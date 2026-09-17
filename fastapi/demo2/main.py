from fastapi import FastAPI
from models import Employee

app = FastAPI()

# Temporary database
employees = []


# CREATE
@app.post("/employees")
def create_employee(employee: Employee):

    employees.append(employee)

    return employee


# READ ALL
@app.get("/employees")
def get_employees():

    return employees


# READ ONE
@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):

    for employee in employees:

        if employee.id == employee_id:
            return employee

    return {"message": "Employee not found"}


# UPDATE
@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, updated_employee: Employee):

    for employee in employees:

        if employee.id == employee_id:

            employee.name = updated_employee.name
            employee.salary = updated_employee.salary

            return employee

    return {"message": "Employee not found"}


# DELETE
@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):

    for employee in employees:

        if employee.id == employee_id:

            employees.remove(employee)

            return {"message": "Employee deleted"}

    return {"message": "Employee not found"}