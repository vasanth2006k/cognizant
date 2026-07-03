from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from database import Base


# ----------------------------------
# Department Model
# ----------------------------------

class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    dept_name = Column(String(100))
    hod_name = Column(String(100))
    budget = Column(Integer)

    courses = relationship(
        "Course",
        back_populates="department",
        cascade="all, delete"
    )

    students = relationship(
        "Student",
        back_populates="department",
        cascade="all, delete"
    )


# ----------------------------------
# Course Model
# ----------------------------------

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)

    course_name = Column(String(150))
    course_code = Column(String(20), unique=True)
    credits = Column(Integer)

    department_id = Column(
        Integer,
        ForeignKey("departments.id")
    )

    department = relationship(
        "Department",
        back_populates="courses"
    )

    enrollments = relationship(
        "Enrollment",
        back_populates="course",
        cascade="all, delete"
    )


# ----------------------------------
# Student Model
# ----------------------------------

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)

    first_name = Column(String(50))
    last_name = Column(String(50))

    email = Column(
        String(100),
        unique=True
    )

    enrollment_year = Column(Integer)

    department_id = Column(
        Integer,
        ForeignKey("departments.id")
    )

    department = relationship(
        "Department",
        back_populates="students"
    )

    enrollments = relationship(
        "Enrollment",
        back_populates="student",
        cascade="all, delete"
    )


# ----------------------------------
# Enrollment Model
# ----------------------------------

class Enrollment(Base):
    __tablename__ = "enrollments"

    id = Column(Integer, primary_key=True, index=True)

    student_id = Column(
        Integer,
        ForeignKey("students.id")
    )

    course_id = Column(
        Integer,
        ForeignKey("courses.id")
    )

    enrollment_date = Column(Date)

    grade = Column(String(2))

    student = relationship(
        "Student",
        back_populates="enrollments"
    )

    course = relationship(
        "Course",
        back_populates="enrollments"
    )


# ----------------------------------
# USER MODEL (Hands-On 9)
# ----------------------------------

class User(Base):
    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    email = Column(
        String(100),
        unique=True,
        nullable=False,
        index=True
    )

    hashed_password = Column(
        String(255),
        nullable=False
    )

    is_active = Column(
        Integer,
        default=1
    )from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from database import Base


# ----------------------------------
# Department Model
# ----------------------------------

class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    dept_name = Column(String(100))
    hod_name = Column(String(100))
    budget = Column(Integer)

    courses = relationship(
        "Course",
        back_populates="department",
        cascade="all, delete"
    )

    students = relationship(
        "Student",
        back_populates="department",
        cascade="all, delete"
    )


# ----------------------------------
# Course Model
# ----------------------------------

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)

    course_name = Column(String(150))
    course_code = Column(String(20), unique=True)
    credits = Column(Integer)

    department_id = Column(
        Integer,
        ForeignKey("departments.id")
    )

    department = relationship(
        "Department",
        back_populates="courses"
    )

    enrollments = relationship(
        "Enrollment",
        back_populates="course",
        cascade="all, delete"
    )


# ----------------------------------
# Student Model
# ----------------------------------

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)

    first_name = Column(String(50))
    last_name = Column(String(50))

    email = Column(
        String(100),
        unique=True
    )

    enrollment_year = Column(Integer)

    department_id = Column(
        Integer,
        ForeignKey("departments.id")
    )

    department = relationship(
        "Department",
        back_populates="students"
    )

    enrollments = relationship(
        "Enrollment",
        back_populates="student",
        cascade="all, delete"
    )


# ----------------------------------
# Enrollment Model
# ----------------------------------

class Enrollment(Base):
    __tablename__ = "enrollments"

    id = Column(Integer, primary_key=True, index=True)

    student_id = Column(
        Integer,
        ForeignKey("students.id")
    )

    course_id = Column(
        Integer,
        ForeignKey("courses.id")
    )

    enrollment_date = Column(Date)

    grade = Column(String(2))

    student = relationship(
        "Student",
        back_populates="enrollments"
    )

    course = relationship(
        "Course",
        back_populates="enrollments"
    )


# ----------------------------------
# USER MODEL (Hands-On 9)
# ----------------------------------

class User(Base):
    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    email = Column(
        String(100),
        unique=True,
        nullable=False,
        index=True
    )

    hashed_password = Column(
        String(255),
        nullable=False
    )

    is_active = Column(
        Integer,
        default=1
    )