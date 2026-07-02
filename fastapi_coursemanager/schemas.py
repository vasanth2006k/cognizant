from pydantic import BaseModel
from typing import Optional
from datetime import date


# ---------------- Department ----------------

class DepartmentBase(BaseModel):
    dept_name: str
    hod_name: str
    budget: int


class DepartmentCreate(DepartmentBase):
    pass


class DepartmentResponse(DepartmentBase):
    id: int

    class Config:
        from_attributes = True


# ---------------- Course ----------------

class CourseBase(BaseModel):
    course_name: str
    course_code: str
    credits: int
    department_id: int


class CourseCreate(CourseBase):
    pass


class CourseUpdate(BaseModel):
    course_name: Optional[str] = None
    course_code: Optional[str] = None
    credits: Optional[int] = None
    department_id: Optional[int] = None


class CourseResponse(CourseBase):
    id: int

    class Config:
        from_attributes = True


# ---------------- Student ----------------

class StudentBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    enrollment_year: int
    department_id: int


class StudentCreate(StudentBase):
    pass


class StudentUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    enrollment_year: Optional[int] = None
    department_id: Optional[int] = None


class StudentResponse(StudentBase):
    id: int

    class Config:
        from_attributes = True


# ---------------- Enrollment ----------------

class EnrollmentBase(BaseModel):
    student_id: int
    course_id: int
    enrollment_date: date
    grade: Optional[str] = None


class EnrollmentCreate(EnrollmentBase):
    pass


class EnrollmentResponse(EnrollmentBase):
    id: int

    class Config:
        from_attributes = True