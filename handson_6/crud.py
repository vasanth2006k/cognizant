from sqlalchemy.orm import (
    sessionmaker,
    joinedload
)

from models import (
    engine,
    Department,
    Student,
    Course,
    Enrollment
)

Session = sessionmaker(
    bind=engine
)

session = Session()


# INSERT DEPARTMENTS


d1 = Department(
    dept_name="Computer Science",
    hod_name="Dr Ramesh",
    budget=850000
)

d2 = Department(
    dept_name="Electronics",
    hod_name="Dr Priya",
    budget=620000
)

d3 = Department(
    dept_name="Mechanical",
    hod_name="Dr Suresh",
    budget=540000
)

session.add_all([d1,d2,d3])

session.commit()

print("Departments inserted")


# INSERT STUDENTS

s1 = Student(
    first_name="Arjun",
    last_name="Mehta",
    email="arjun@gmail.com",
    department=d1,
    enrollment_year=2022
)

s2 = Student(
    first_name="Priya",
    last_name="Suresh",
    email="priya@gmail.com",
    department=d1,
    enrollment_year=2022
)

s3 = Student(
    first_name="Rohan",
    last_name="Verma",
    email="rohan@gmail.com",
    department=d2,
    enrollment_year=2021
)

s4 = Student(
    first_name="Sneha",
    last_name="Patel",
    email="sneha@gmail.com",
    department=d3,
    enrollment_year=2023
)

s5 = Student(
    first_name="Deepika",
    last_name="Rao",
    email="deepika@gmail.com",
    department=d1,
    enrollment_year=2022
)

session.add_all(
[
s1,
s2,
s3,
s4,
s5
]
)

session.commit()

print("Students inserted")


# ADD COURSES

c1 = Course(
    course_name="DSA",
    course_code="CS101",
    credits=4,
    department=d1
)

c2 = Course(
    course_name="DBMS",
    course_code="CS102",
    credits=3,
    department=d1
)

c3 = Course(
    course_name="Circuit Theory",
    course_code="EC101",
    credits=3,
    department=d2
)

session.add_all(
[
c1,
c2,
c3
]
)

session.commit()



# ADD ENROLLMENTS

e1 = Enrollment(
    student=s1,
    course=c1
)

e2 = Enrollment(
    student=s1,
    course=c2
)

e3 = Enrollment(
    student=s2,
    course=c1
)

e4 = Enrollment(
    student=s3,
    course=c3
)

session.add_all(
[
e1,
e2,
e3,
e4
]
)

session.commit()

print("Enrollments inserted")


# READ OPERATION

students = (
session.query(Student)
.join(Department)
.filter(
Department.dept_name=="Computer Science"
)
.all()
)

print("\nComputer Science Students")

for s in students:

    print(
        s.first_name,
        s.last_name
    )


# DISPLAY ENROLLMENTS

enrollments = (
session.query(Enrollment)
.all()
)

for e in enrollments:

    print(
        e.student.first_name,
        "-",
        e.course.course_name
    )



# UPDATE

student = (
session.query(Student)
.filter_by(
email="arjun@gmail.com"
)
.first()
)

student.enrollment_year = 2024

session.commit()

print("Updated")



# DELETE


obj = (
session.query(Enrollment)
.first()
)

session.delete(obj)

session.commit()

print("Deleted")


#################
# FIX N+1
#################

data = (
session.query(Enrollment)
.options(
joinedload(
Enrollment.student
),

joinedload(
Enrollment.course
)
)
.all()
)

for d in data:

    print(
        d.student.first_name,
        d.course.course_name
    )


session.close()