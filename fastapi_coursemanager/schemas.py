from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date


# ======================================
# Department Schemas
# ======================================

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


# ======================================
# Course Schemas
# ======================================

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


# ======================================
# Student Schemas
# ======================================

class StudentBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    enrollment_year: int
    department_id: int


class StudentCreate(StudentBase):
    pass


class StudentUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    enrollment_year: Optional[int] = None
    department_id: Optional[int] = None


class StudentResponse(StudentBase):
    id: int

    class Config:
        from_attributes = True


# ======================================
# Enrollment Schemas
# ======================================

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


# ======================================
# User Registration (Hands-On 9)
# ======================================

class UserRegister(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    is_active: int

    class Config:
        from_attributes = True


# ======================================
# JWT Token Schemas
# ======================================

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None