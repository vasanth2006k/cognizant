from pydantic import BaseModel
from typing import Optional, List


# -----------------------------
# Course Create Schema
# -----------------------------
class CourseCreate(BaseModel):
    course_name: str
    course_code: str
    credits: int
    department_id: int


# -----------------------------
# Course Update Schema
# All fields are optional
# -----------------------------
class CourseUpdate(BaseModel):
    course_name: Optional[str] = None
    course_code: Optional[str] = None
    credits: Optional[int] = None
    department_id: Optional[int] = None


# -----------------------------
# Course Response Schema
# -----------------------------
class CourseResponse(BaseModel):
    id: int
    course_name: str
    course_code: str
    credits: int
    department_id: int

    class Config:
        from_attributes = True


# -----------------------------
# Department Response Schema
# -----------------------------
class DepartmentResponse(BaseModel):
    id: int
    dept_name: str
    hod_name: str
    budget: float

    courses: List[CourseResponse] = []

    class Config:
        from_attributes = True