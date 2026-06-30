from extensions import db


class Department(db.Model):
    __tablename__ = "departments"

    id = db.Column(db.Integer, primary_key=True)

    dept_name = db.Column(
        db.String(100),
        nullable=False
    )

    hod_name = db.Column(
        db.String(100),
        nullable=False
    )

    budget = db.Column(
        db.Float,
        nullable=False
    )

    courses = db.relationship(
        "Course",
        back_populates="department",
        cascade="all, delete-orphan"
    )

    students = db.relationship(
        "Student",
        back_populates="department",
        cascade="all, delete-orphan"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "dept_name": self.dept_name,
            "hod_name": self.hod_name,
            "budget": self.budget
        }


class Course(db.Model):
    __tablename__ = "courses"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    course_name = db.Column(
        db.String(150),
        nullable=False
    )

    course_code = db.Column(
        db.String(20),
        unique=True,
        nullable=False
    )

    credits = db.Column(
        db.Integer,
        nullable=False
    )

    department_id = db.Column(
        db.Integer,
        db.ForeignKey("departments.id"),
        nullable=False
    )

    department = db.relationship(
        "Department",
        back_populates="courses"
    )

    enrollments = db.relationship(
        "Enrollment",
        back_populates="course",
        cascade="all, delete-orphan"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "course_name": self.course_name,
            "course_code": self.course_code,
            "credits": self.credits,
            "department_id": self.department_id
        }


class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    first_name = db.Column(
        db.String(50),
        nullable=False
    )

    last_name = db.Column(
        db.String(50),
        nullable=False
    )

    email = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    enrollment_year = db.Column(
        db.Integer,
        nullable=False
    )

    department_id = db.Column(
        db.Integer,
        db.ForeignKey("departments.id"),
        nullable=False
    )

    department = db.relationship(
        "Department",
        back_populates="students"
    )

    enrollments = db.relationship(
        "Enrollment",
        back_populates="student",
        cascade="all, delete-orphan"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "enrollment_year": self.enrollment_year,
            "department_id": self.department_id
        }


class Enrollment(db.Model):
    __tablename__ = "enrollments"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    student_id = db.Column(
        db.Integer,
        db.ForeignKey("students.id"),
        nullable=False
    )

    course_id = db.Column(
        db.Integer,
        db.ForeignKey("courses.id"),
        nullable=False
    )

    enrollment_date = db.Column(
        db.Date,
        nullable=False
    )

    grade = db.Column(
        db.String(2),
        nullable=True
    )

    student = db.relationship(
        "Student",
        back_populates="enrollments"
    )

    course = db.relationship(
        "Course",
        back_populates="enrollments"
    )

    __table_args__ = (
        db.UniqueConstraint(
            "student_id",
            "course_id",
            name="unique_enrollment"
        ),
    )

    def to_dict(self):
        return {
            "id": self.id,
            "student_id": self.student_id,
            "course_id": self.course_id,
            "enrollment_date": str(self.enrollment_date),
            "grade": self.grade
        }