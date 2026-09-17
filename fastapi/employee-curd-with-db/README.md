# Employee CRUD API (FastAPI + MySQL)

A simple, layered **Employee Management REST API** built with **FastAPI** and **SQLAlchemy**, backed by a **MySQL** database. This project demonstrates a clean architecture (routers → services → repositories → models) for performing **CRUD** (Create, Read, Update, Delete) operations on employee records.

---

## Table of Contents

- [What is FastAPI?](#what-is-fastapi)
- [Why this project structure?](#why-this-project-structure)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
- [Running the Application](#running-the-application)
- [Interactive API Docs](#interactive-api-docs)
- [API Reference](#api-reference)
  - [1. Health Check](#1-health-check)
  - [2. Create Employee](#2-create-employee)
  - [3. Get All Employees](#3-get-all-employees)
  - [4. Get Employee by ID](#4-get-employee-by-id)
  - [5. Update Employee](#5-update-employee)
  - [6. Delete Employee](#6-delete-employee)
- [Data Model](#data-model)
- [Error Handling](#error-handling)
- [How a Request Flows Through the App](#how-a-request-flows-through-the-app)

---

## What is FastAPI?

[FastAPI](https://fastapi.tiangolo.com/) is a modern, high-performance Python web framework used for building APIs. Key highlights:

- **Fast**: Built on top of `Starlette` (web layer) and `Pydantic` (data validation), and is one of the fastest Python frameworks available.
- **Type-hint driven**: You declare request/response shapes using standard Python type hints, and FastAPI automatically validates, serializes, and documents them.
- **Automatic interactive docs**: FastAPI generates **Swagger UI** (`/docs`) and **ReDoc** (`/redoc`) documentation automatically from your code — no extra work needed.
- **Dependency Injection**: Built-in support for things like database sessions (`Depends(get_db)`), authentication, etc.
- **Async-ready**: Supports both `async def` and regular `def` route handlers.

In this project, FastAPI is responsible for:
- Defining HTTP routes (`GET`, `POST`, `PUT`, `DELETE`)
- Validating incoming JSON using **Pydantic schemas**
- Returning JSON responses with the correct shape and status codes
- Auto-generating the `/docs` page you can test the API from

---

## Why this project structure?

Instead of putting everything in one file, the app is split into layers, each with a single responsibility:

| Layer | Folder | Responsibility |
|---|---|---|
| **Entry point** | `app/main.py` | Creates the FastAPI app, creates DB tables, registers routers |
| **Router** | `app/routers/` | Defines API endpoints (URLs, HTTP methods), delegates to services |
| **Schema** | `app/schemas/` | Pydantic models for validating input and shaping output (API contract) |
| **Service** | `app/services/` | Business logic — converts schema data into DB models and calls repository |
| **Repository** | `app/repositories/` | Direct database operations (add, query, commit, delete) |
| **Model** | `app/models/` | SQLAlchemy ORM models — represents actual database tables |
| **Database** | `app/database/` | DB connection/engine setup and session management |

This separation makes the code easier to test, maintain, and extend (e.g., swapping MySQL for PostgreSQL only requires changing `connection.py`).

---

## Project Structure

```
employee-curd-with-db/
└── app/
    ├── main.py                      # FastAPI app entry point
    ├── database/
    │   ├── __init__.py
    │   └── connection.py            # MySQL engine, session, Base, get_db()
    ├── models/
    │   ├── __init__.py
    │   └── employee.py              # SQLAlchemy "employees" table model
    ├── schemas/
    │   ├── __init__.py
    │   └── employee.py              # Pydantic request/response schemas
    ├── repositories/
    │   ├── __init__.py
    │   └── employee_repository.py   # Raw DB CRUD operations
    ├── services/
    │   ├── __init__.py
    │   └── employee_service.py      # Business logic layer
    └── routers/
        ├── __init__.py
        └── employee_router.py       # API route definitions
```

---

## Requirements

- Python 3.9+
- MySQL Server running locally (or reachable)
- Python packages:
  - `fastapi`
  - `uvicorn`
  - `sqlalchemy`
  - `pymysql`

Install dependencies:

```bash
pip install fastapi uvicorn sqlalchemy pymysql
```

---

## Setup Instructions

1. **Create the MySQL database** referenced in [connection.py](app/database/connection.py):

   ```sql
   CREATE DATABASE employee_db;
   ```

2. **Update the connection string** if your MySQL username/password/host differ from the default:

   ```python
   # app/database/connection.py
   DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/employee_db"
   ```

3. The `employees` table is created automatically on startup via:

   ```python
   Base.metadata.create_all(bind=engine)
   ```

   No manual migration step is required for this simple project.

---

## Running the Application

From the `employee-curd-with-db` folder, run:

```bash
uvicorn app.main:app --reload
```

- `app.main:app` → points to the `app` FastAPI instance inside `app/main.py`
- `--reload` → automatically restarts the server when code changes (useful during development)

By default, the API will be available at:

```
http://127.0.0.1:8000
```

---

## Interactive API Docs

FastAPI automatically generates interactive documentation:

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

You can test every endpoint directly from the browser without needing Postman or curl.

---

## API Reference

Base URL: `http://127.0.0.1:8000`

### 1. Health Check

Simple endpoint to verify the API is running.

| Method | Endpoint |
|---|---|
| GET | `/` |

**Sample Response — 200 OK**
```json
{
  "message": "Employee CRUD API is running"
}
```

---

### 2. Create Employee

Creates a new employee record.

| Method | Endpoint |
|---|---|
| POST | `/employees` |

**Sample Request Body**
```json
{
  "name": "Alice Johnson",
  "email": "alice.johnson@example.com",
  "department": "Engineering",
  "salary": 75000.00
}
```

**Sample Response — 200 OK**
```json
{
  "id": 1,
  "name": "Alice Johnson",
  "email": "alice.johnson@example.com",
  "department": "Engineering",
  "salary": 75000.00
}
```

---

### 3. Get All Employees

Retrieves all employee records.

| Method | Endpoint |
|---|---|
| GET | `/employees` |

**Sample Response — 200 OK**
```json
[
  {
    "id": 1,
    "name": "Alice Johnson",
    "email": "alice.johnson@example.com",
    "department": "Engineering",
    "salary": 75000.00
  },
  {
    "id": 2,
    "name": "Bob Smith",
    "email": "bob.smith@example.com",
    "department": "Marketing",
    "salary": 62000.50
  }
]
```

---

### 4. Get Employee by ID

Retrieves a single employee by their ID.

| Method | Endpoint |
|---|---|
| GET | `/employees/{employee_id}` |

**Sample Request**
```
GET /employees/1
```

**Sample Response — 200 OK**
```json
{
  "id": 1,
  "name": "Alice Johnson",
  "email": "alice.johnson@example.com",
  "department": "Engineering",
  "salary": 75000.00
}
```

**Sample Response — 404 Not Found**
```json
{
  "detail": "Employee not found"
}
```

---

### 5. Update Employee

Updates an existing employee's details. All fields are required (full replace).

| Method | Endpoint |
|---|---|
| PUT | `/employees/{employee_id}` |

**Sample Request**
```
PUT /employees/1
```

**Sample Request Body**
```json
{
  "name": "Alice Johnson",
  "email": "alice.j@example.com",
  "department": "Product",
  "salary": 82000.00
}
```

**Sample Response — 200 OK**
```json
{
  "id": 1,
  "name": "Alice Johnson",
  "email": "alice.j@example.com",
  "department": "Product",
  "salary": 82000.00
}
```

**Sample Response — 404 Not Found**
```json
{
  "detail": "Employee not found"
}
```

---

### 6. Delete Employee

Deletes an employee by ID.

| Method | Endpoint |
|---|---|
| DELETE | `/employees/{employee_id}` |

**Sample Request**
```
DELETE /employees/1
```

**Sample Response — 200 OK**
```json
{
  "message": "Employee deleted successfully"
}
```

**Sample Response — 404 Not Found**
```json
{
  "detail": "Employee not found"
}
```

---

## Data Model

The `employees` table (defined in [app/models/employee.py](app/models/employee.py)):

| Column | Type | Constraints |
|---|---|---|
| `id` | Integer | Primary key, indexed, auto-generated |
| `name` | String(100) | Required |
| `email` | String(150) | Required, unique |
| `department` | String(100) | Required |
| `salary` | Float | Required |

Request/response validation is handled by Pydantic schemas in [app/schemas/employee.py](app/schemas/employee.py):

- `EmployeeCreate` — used for `POST` and `PUT` request bodies (`name`, `email`, `department`, `salary`)
- `EmployeeResponse` — used for all responses (adds `id`, and converts SQLAlchemy objects to JSON via `from_attributes = True`)

---

## Error Handling

- Requests with an invalid body (e.g., missing fields, wrong types) automatically return **422 Unprocessable Entity** with details about which field failed validation — this is handled by FastAPI/Pydantic without any extra code.
- Requests for an employee ID that doesn't exist return **404 Not Found** with a `detail` message, raised explicitly in [employee_router.py](app/routers/employee_router.py) using `HTTPException`.
- Duplicate emails will fail at the database level due to the `unique=True` constraint on the `email` column.

---

## How a Request Flows Through the App

```mermaid
sequenceDiagram
    participant Client
    participant Router as employee_router.py
    participant Service as employee_service.py
    participant Repo as employee_repository.py
    participant DB as MySQL (employees table)

    Client->>Router: HTTP request (e.g. POST /employees)
    Router->>Router: Validate body with EmployeeCreate schema
    Router->>Service: create_employee(db, employee)
    Service->>Service: Build Employee ORM object
    Service->>Repo: create_employee(db, employee)
    Repo->>DB: INSERT INTO employees ...
    DB-->>Repo: New row (with id)
    Repo-->>Service: Employee object
    Service-->>Router: Employee object
    Router-->>Client: JSON response (EmployeeResponse)
```

This layered flow (**Router → Service → Repository → Database**) keeps each part focused on a single job, making the API easy to extend (e.g., add validation rules, caching, or swap the database) without rewriting the whole app.
