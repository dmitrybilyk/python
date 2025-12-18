from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# ------------------
# CORS
# ------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------
# Models
# ------------------
class Department(BaseModel):
    id: int
    name: str


class Employee(BaseModel):
    id: int
    name: str
    department_id: int


# ------------------
# In-memory DATA
# ------------------
departments = {
    1: Department(id=1, name="IT"),
    2: Department(id=2, name="HR"),
    3: Department(id=3, name="Finance"),
}

employees = {
    1: Employee(id=1, name="Alice", department_id=1),
    2: Employee(id=2, name="Bob", department_id=1),
    3: Employee(id=3, name="Carol", department_id=2),
    4: Employee(id=4, name="Dave", department_id=3),
}

# ------------------
# Endpoints
# ------------------
@app.get("/departments", response_model=List[Department])
def get_departments():
    return list(departments.values())


@app.get("/employees", response_model=List[Employee])
def get_employees():
    return list(employees.values())


@app.get("/departments/{dept_id}/employees",
         response_model=List[Employee])
def get_employees_by_department(dept_id: int):
    return [
        e for e in employees.values()
        if e.department_id == dept_id
    ]
