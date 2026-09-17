# FastAPI Interview Questions (Easy → Advanced)

A complete set of FastAPI + SQLAlchemy interview questions, explained in **simple words** with **short code examples**. Questions go from basic concepts to advanced topics, so this file works for beginners as well as experienced developers preparing for interviews.

> Tip: The code snippets are intentionally short — just enough to prove the concept, similar to the style used in this project (`employee-curd-with-db`).

---

## Table of Contents

- [Level 1: Easy (Basics)](#level-1-easy-basics)
- [Level 2: Intermediate](#level-2-intermediate)
- [Level 3: Advanced](#level-3-advanced)
- [Level 4: Database (SQLAlchemy) Questions](#level-4-database-sqlalchemy-questions)
- [Level 5: Scenario / Project-Based Questions](#level-5-scenario--project-based-questions)
- [Quick Cheat Sheet](#quick-cheat-sheet)

---

## Level 1: Easy (Basics)

### Q1. What is FastAPI?

**Simple explanation:** FastAPI is a Python framework used to build APIs (backend services) quickly. It is fast, easy to write, and automatically creates documentation for your API.

**Key points:**
- Built on top of **Starlette** (handles web requests) and **Pydantic** (handles data validation).
- Uses normal Python type hints — no special syntax to learn.
- Automatically generates Swagger UI docs at `/docs`.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}
```

---

### Q2. Why use FastAPI instead of Flask or Django?

**Simple explanation:** FastAPI is faster to run, faster to write, and gives you free features that you'd have to build yourself in Flask.

| Feature | FastAPI | Flask |
|---|---|---|
| Data validation | Built-in (Pydantic) | Manual |
| Auto docs (Swagger) | Yes | No (needs extension) |
| Async support | Native | Limited |
| Type hints | Required/used | Optional, not used |
| Performance | Very high (Starlette + async) | Moderate |

---

### Q3. How do you install and run a FastAPI app?

```bash
pip install fastapi uvicorn
uvicorn main:app --reload
```

**Simple explanation:**
- `fastapi` → the framework itself.
- `uvicorn` → the server that actually runs your app (FastAPI doesn't run itself).
- `main:app` → means "look inside `main.py` for a variable called `app`".
- `--reload` → restarts server automatically when you save code changes (dev only).

---

### Q4. What is a path parameter?

**Simple explanation:** A value that comes from the URL itself.

```python
@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    return {"id": employee_id}
```

Calling `GET /employees/5` → `employee_id = 5`. FastAPI automatically converts it to `int` and returns a `422` error if you send text like `"abc"`.

---

### Q5. What is a query parameter?

**Simple explanation:** Extra values passed after `?` in the URL, usually used for optional filters, search, or pagination.

```python
@app.get("/employees")
def get_employees(department: str = None, limit: int = 10):
    return {"department": department, "limit": limit}
```

Call it like: `GET /employees?department=Engineering&limit=5`

---

### Q6. What is a request body, and how do you read one?

**Simple explanation:** Data sent by the client (usually JSON) in `POST`/`PUT` requests. FastAPI uses a **Pydantic model** to read and validate it.

```python
from pydantic import BaseModel

class Employee(BaseModel):
    name: str
    salary: float

@app.post("/employees")
def create_employee(employee: Employee):
    return employee
```

---

### Q7. What is Pydantic, and why does FastAPI use it?

**Simple explanation:** Pydantic checks that the data you receive matches the type you expect (e.g., `salary` must be a number, not text). If it doesn't match, FastAPI automatically sends back a clear `422` error — you don't write that validation code yourself.

```python
class EmployeeCreate(BaseModel):
    name: str
    email: str
    salary: float
```

If someone sends `"salary": "abc"`, FastAPI rejects it automatically before your code even runs.

---

### Q8. What HTTP methods does FastAPI support, and what are they used for?

| Method | Decorator | Used for |
|---|---|---|
| GET | `@app.get()` | Read/fetch data |
| POST | `@app.post()` | Create new data |
| PUT | `@app.put()` | Update/replace existing data |
| PATCH | `@app.patch()` | Partially update data |
| DELETE | `@app.delete()` | Remove data |

---

### Q9. How does FastAPI generate documentation automatically?

**Simple explanation:** FastAPI reads your route definitions, type hints, and Pydantic models, then builds interactive docs without any extra work.

- Swagger UI → `http://127.0.0.1:8000/docs`
- ReDoc → `http://127.0.0.1:8000/redoc`

---

### Q10. What status code does FastAPI return by default, and how do you change it?

**Simple explanation:** Default is `200 OK` for success. You can customize it per route.

```python
from fastapi import status

@app.post("/employees", status_code=status.HTTP_201_CREATED)
def create_employee(employee: Employee):
    return employee
```

---

## Level 2: Intermediate

### Q11. What is Dependency Injection in FastAPI, and how does `Depends` work?

**Simple explanation:** Instead of creating things (like a database session) manually inside every function, you tell FastAPI "give me this thing when the request comes in." FastAPI calls the function for you and passes the result in.

```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/employees")
def get_employees(db: Session = Depends(get_db)):
    return db.query(Employee).all()
```

**Why it's useful:** Every request gets its own fresh database session, and the session is automatically closed after the request — even if an error happens.

---

### Q12. What is a `response_model`, and why use it?

**Simple explanation:** It defines exactly what shape of data the API sends back — even if your database object has more/fewer fields. It also filters out any sensitive fields you don't want to expose.

```python
class EmployeeResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True  # allows converting SQLAlchemy objects to this schema

@app.get("/employees/{id}", response_model=EmployeeResponse)
def get_employee(id: int):
    ...
```

---

### Q13. What is `APIRouter`, and why split routes into separate files?

**Simple explanation:** `APIRouter` lets you group related routes (like all Employee routes) into their own file, then plug them into the main app. This keeps large projects organized.

```python
# employee_router.py
from fastapi import APIRouter
router = APIRouter(prefix="/employees", tags=["Employees"])

@router.get("")
def get_all_employees():
    return []
```

```python
# main.py
from fastapi import FastAPI
from employee_router import router

app = FastAPI()
app.include_router(router)
```

---

### Q14. How does FastAPI handle errors like "not found"?

**Simple explanation:** Use `HTTPException` to stop execution and return a specific status code + message.

```python
from fastapi import HTTPException

@app.get("/employees/{id}")
def get_employee(id: int):
    employee = find_employee(id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee
```

---

### Q15. What is the difference between `def` and `async def` route functions in FastAPI?

**Simple explanation:**
- `async def` → non-blocking. Good when calling things like async database drivers or external APIs — lets FastAPI handle other requests while waiting.
- `def` (normal function) → FastAPI automatically runs it in a separate thread pool, so it still won't block the whole server, but it's used when your code isn't `async`-based (e.g., regular SQLAlchemy).

```python
@app.get("/sync")
def sync_route():
    return {"type": "regular function"}

@app.get("/async")
async def async_route():
    return {"type": "async function"}
```

---

### Q16. How do you validate data further (e.g., minimum length, ranges) in Pydantic?

```python
from pydantic import BaseModel, Field, EmailStr

class EmployeeCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    salary: float = Field(gt=0)  # salary must be greater than 0
```

**Simple explanation:** `Field()` lets you add extra rules to a property. `EmailStr` even checks it's a real email format.

---

### Q17. What are FastAPI's built-in status code helpers, and why use them instead of raw numbers?

```python
from fastapi import status

status.HTTP_200_OK        # 200
status.HTTP_201_CREATED   # 201
status.HTTP_404_NOT_FOUND # 404
status.HTTP_422_UNPROCESSABLE_ENTITY  # 422
```

**Simple explanation:** More readable than hardcoding `404` everywhere, and less error-prone (autocomplete helps you pick the right one).

---

### Q18. What is CORS, and how do you enable it in FastAPI?

**Simple explanation:** CORS (Cross-Origin Resource Sharing) controls which websites/domains are allowed to call your API from a browser. Without it, a frontend on a different domain/port gets blocked.

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

### Q19. What is middleware in FastAPI?

**Simple explanation:** Code that runs **before and after every request**, useful for logging, timing, authentication checks, etc.

```python
@app.middleware("http")
async def log_requests(request, call_next):
    print(f"Incoming request: {request.url}")
    response = await call_next(request)
    return response
```

---

### Q20. How do you handle optional fields in request bodies (e.g., for PATCH-style partial updates)?

```python
from typing import Optional

class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    salary: Optional[float] = None
```

**Simple explanation:** If a field is `Optional` with a default (`None`), the client doesn't have to send it, which is perfect for partial updates.

---

## Level 3: Advanced

### Q21. How do you implement authentication (OAuth2 / JWT) in FastAPI?

**Simple explanation:** FastAPI has built-in support for OAuth2 password flow. The client sends username/password, gets a token back, and sends that token on future requests.

```python
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/profile")
def read_profile(token: str = Depends(oauth2_scheme)):
    return {"token": token}
```

Typically combined with the `python-jose` library to create/verify JWT tokens.

---

### Q22. What are Background Tasks in FastAPI?

**Simple explanation:** Run something **after** sending the response to the client — e.g., sending an email after account creation, without making the client wait.

```python
from fastapi import BackgroundTasks

def send_email(email: str):
    print(f"Sending email to {email}")

@app.post("/register")
def register(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email, email)
    return {"message": "Registered! Email will be sent shortly."}
```

---

### Q23. How do you write custom exception handlers?

**Simple explanation:** Instead of repeating error-handling logic, define one handler for a custom exception type used across the whole app.

```python
from fastapi import Request
from fastapi.responses import JSONResponse

class EmployeeNotFoundError(Exception):
    pass

@app.exception_handler(EmployeeNotFoundError)
def handle_not_found(request: Request, exc: EmployeeNotFoundError):
    return JSONResponse(status_code=404, content={"detail": "Employee not found"})
```

---

### Q24. How do you test a FastAPI application?

**Simple explanation:** FastAPI provides `TestClient` (built on `httpx`/`requests`) to call your endpoints in tests without running a real server.

```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Employee CRUD API is running"}
```

---

### Q25. What is the difference between `Depends` with a function vs. a class?

**Simple explanation:** Class-based dependencies are useful when the dependency needs configuration (parameters) or shared state.

```python
class Pagination:
    def __init__(self, skip: int = 0, limit: int = 10):
        self.skip = skip
        self.limit = limit

@app.get("/employees")
def get_employees(pagination: Pagination = Depends()):
    return {"skip": pagination.skip, "limit": pagination.limit}
```

---

### Q26. How does FastAPI handle concurrency/performance internally?

**Simple explanation:** FastAPI is built on **ASGI** (Asynchronous Server Gateway Interface) via Starlette, and runs on **Uvicorn**, which uses an event loop (`asyncio`). This means it can handle many requests at once without opening a new thread for each one, especially when using `async def` with non-blocking I/O (e.g., async DB drivers, `httpx` calls).

---

### Q27. What is API versioning, and how would you implement it in FastAPI?

**Simple explanation:** Keep old API behavior working for existing clients while introducing new versions.

```python
from fastapi import APIRouter

v1_router = APIRouter(prefix="/v1")
v2_router = APIRouter(prefix="/v2")

app.include_router(v1_router)
app.include_router(v2_router)
```

---

### Q28. How do you implement pagination in a FastAPI + SQLAlchemy endpoint?

```python
@app.get("/employees")
def get_employees(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Employee).offset(skip).limit(limit).all()
```

**Simple explanation:** `offset` skips a number of rows, `limit` caps how many rows are returned — standard way to paginate large result sets.

---

### Q29. What are Pydantic `model_config` / `Config` and `from_attributes` used for?

**Simple explanation:** By default, Pydantic models expect dictionaries. Setting `from_attributes = True` (formerly `orm_mode = True` in Pydantic v1) tells Pydantic it's OK to read data from an object's attributes (like a SQLAlchemy model), not just from a dict.

```python
class EmployeeResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
```

---

### Q30. How would you structure a large FastAPI project (layered architecture)?

**Simple explanation:** Split responsibilities into layers so each file has one job — same pattern used in this repo.

```
routers/     -> defines endpoints (URL + HTTP method)
schemas/     -> Pydantic models (input/output validation)
services/    -> business logic
repositories/-> raw database operations
models/      -> SQLAlchemy table definitions
database/    -> engine/session setup
```

**Why:** Easier testing (mock a layer), easier maintenance, and clear separation between "what the API looks like" and "how data is stored."

---

## Level 4: Database (SQLAlchemy) Questions

### Q31. What is SQLAlchemy, and why use it with FastAPI?

**Simple explanation:** SQLAlchemy is an ORM (Object Relational Mapper) — it lets you work with database tables using Python classes and objects instead of writing raw SQL.

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
```

---

### Q32. What is the difference between `engine`, `Session`, and `Base` in SQLAlchemy?

| Term | Simple meaning |
|---|---|
| `engine` | The actual connection to the database (knows the DB URL, driver) |
| `SessionLocal`/`Session` | A "workspace" used to talk to the DB for one request (add, query, commit) |
| `Base` | The parent class all your table models inherit from |

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("mysql+pymysql://root:root@localhost:3306/employee_db")
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
```

---

### Q33. Why use `yield` inside `get_db()` instead of `return`?

```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

**Simple explanation:** `yield` pauses the function, hands the session to your route, and after the request finishes, execution resumes at `finally` to close the session — guaranteeing the database connection is always closed, even if an error occurs mid-request.

---

### Q34. How do you perform CRUD operations using SQLAlchemy?

```python
# CREATE
db.add(employee)
db.commit()
db.refresh(employee)

# READ (all)
db.query(Employee).all()

# READ (one)
db.query(Employee).filter(Employee.id == 1).first()

# UPDATE
employee.name = "New Name"
db.commit()

# DELETE
db.delete(employee)
db.commit()
```

---

### Q35. What does `Base.metadata.create_all(bind=engine)` do?

**Simple explanation:** It looks at all your model classes (that inherit from `Base`) and creates the matching tables in the database — but only if they don't already exist. It won't alter existing tables (that's what migration tools like Alembic are for).

---

### Q36. What is the difference between `unique=True`, `nullable=False`, and `index=True` on a Column?

```python
email = Column(String(150), unique=True, nullable=False, index=True)
```

| Option | Meaning |
|---|---|
| `unique=True` | No two rows can have the same value |
| `nullable=False` | The value is required (can't be empty/NULL) |
| `index=True` | Creates a database index for faster searching |

---

### Q37. What is a database migration, and why doesn't this project have one?

**Simple explanation:** A migration is a versioned script that changes your database schema over time (e.g., adding a column later without losing data). Tools like **Alembic** manage this. Small projects (like this one) often just use `create_all()` since the schema rarely changes — but production apps should use Alembic.

---

### Q38. What is a `relationship()` in SQLAlchemy, and when would you use it?

**Simple explanation:** Used to link two tables together (like Employee → Department), so you can access related data as Python objects instead of writing manual JOIN queries.

```python
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    employees = relationship("Employee", back_populates="department")

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True)
    department_id = Column(Integer, ForeignKey("departments.id"))
    department = relationship("Department", back_populates="employees")
```

---

## Level 5: Scenario / Project-Based Questions

### Q39. In this project, walk through what happens when you call `POST /employees`.

**Simple explanation (step by step):**
1. `employee_router.py` receives the request and validates the JSON body against `EmployeeCreate`.
2. The router calls `employee_service.create_employee(db, employee)`.
3. The service converts the Pydantic schema into an `Employee` SQLAlchemy object.
4. The service calls `employee_repository.create_employee(db, employee)`.
5. The repository does `db.add()`, `db.commit()`, `db.refresh()` to save it to MySQL.
6. The saved object (now with an `id`) flows back up through service → router.
7. FastAPI converts it into `EmployeeResponse` JSON and sends it to the client.

---

### Q40. Why does the router not talk directly to the repository?

**Simple explanation:** Keeping the router "thin" (only handling HTTP concerns) and pushing logic into services keeps the code organized. If business rules change (e.g., "salary can't be updated without manager approval"), you only touch `employee_service.py`, not the routes or the database code.

---

### Q41. What would you change to switch this project from MySQL to PostgreSQL?

**Simple explanation:** Only the connection layer needs to change — that's the benefit of using an ORM.

```python
# Before (MySQL)
DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/employee_db"

# After (PostgreSQL)
DATABASE_URL = "postgresql+psycopg2://root:root@localhost:5432/employee_db"
```
Also install `psycopg2` instead of `pymysql`. No changes needed in models, schemas, services, or routers.

---

### Q42. How would you prevent duplicate employee emails from crashing the app with a raw database error?

**Simple explanation:** Catch the `IntegrityError` from SQLAlchemy and turn it into a clean `HTTPException`.

```python
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

def create_employee(db, employee):
    try:
        db.add(employee)
        db.commit()
        db.refresh(employee)
        return employee
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Email already exists")
```

---

### Q43. How would you add search/filtering (e.g., by department) to the `GET /employees` endpoint?

```python
@router.get("")
def get_all_employees(department: str = None, db: Session = Depends(get_db)):
    query = db.query(Employee)
    if department:
        query = query.filter(Employee.department == department)
    return query.all()
```

---

### Q44. How would you add unit tests for the employee service layer without touching a real database?

**Simple explanation:** Use a fake/mock database session (or an in-memory SQLite DB) so tests run fast and don't depend on MySQL being available.

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///:memory:")
TestingSessionLocal = sessionmaker(bind=engine)
```

---

## Quick Cheat Sheet

| Concept | Syntax |
|---|---|
| Create app | `app = FastAPI()` |
| GET route | `@app.get("/path")` |
| POST route | `@app.post("/path")` |
| Path param | `def f(id: int):` with `"/items/{id}"` |
| Query param | `def f(limit: int = 10):` |
| Request body | `def f(item: PydanticModel):` |
| Dependency | `Depends(get_db)` |
| Response shaping | `@app.get(..., response_model=Schema)` |
| Raise error | `raise HTTPException(status_code=404, detail="...")` |
| Router grouping | `APIRouter(prefix="/x", tags=["X"])` |
| Run server | `uvicorn main:app --reload` |
| DB session | `SessionLocal()` via `sessionmaker(bind=engine)` |
| ORM model | `class X(Base): __tablename__ = "x"` |
| Create tables | `Base.metadata.create_all(bind=engine)` |
| CRUD (create) | `db.add(obj); db.commit(); db.refresh(obj)` |
| CRUD (read) | `db.query(Model).all()` / `.filter(...).first()` |
| CRUD (delete) | `db.delete(obj); db.commit()` |

---

**Good luck with your interview!** Practice explaining each answer in your own words and be ready to write the matching small code snippet on a whiteboard or in a live coding round.
