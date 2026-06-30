from flask import Blueprint, request, jsonify
from extensions import db
from .models import Department, Course, Student, Enrollment

courses_bp = Blueprint(
    "courses",
    __name__,
    url_prefix="/api/courses"
)


# ---------------------------------------
# GET ALL COURSES
# ---------------------------------------
@courses_bp.route("/", methods=["GET"])
def get_courses():

    courses = Course.query.all()

    return jsonify(
        [course.to_dict() for course in courses]
    )


# ---------------------------------------
# GET COURSE BY ID
# ---------------------------------------
@courses_bp.route("/<int:id>", methods=["GET"])
def get_course(id):

    course = Course.query.get_or_404(id)

    return jsonify(course.to_dict())


# ---------------------------------------
# ADD COURSE
# ---------------------------------------
@courses_bp.route("/", methods=["POST"])
def add_course():

    data = request.get_json()

    department = Department.query.get(data["department_id"])

    if department is None:
        return jsonify({
            "message": "Department not found"
        }), 404

    course = Course(
        course_name=data["course_name"],
        course_code=data["course_code"],
        credits=data["credits"],
        department_id=data["department_id"]
    )

    db.session.add(course)
    db.session.commit()

    return jsonify(course.to_dict()), 201


# ---------------------------------------
# UPDATE COURSE
# ---------------------------------------
@courses_bp.route("/<int:id>", methods=["PUT"])
def update_course(id):

    course = Course.query.get_or_404(id)

    data = request.get_json()

    if "course_name" in data:
        course.course_name = data["course_name"]

    if "course_code" in data:
        course.course_code = data["course_code"]

    if "credits" in data:
        course.credits = data["credits"]

    if "department_id" in data:

        department = Department.query.get(data["department_id"])

        if department is None:
            return jsonify({
                "message": "Department not found"
            }), 404

        course.department_id = data["department_id"]

    db.session.commit()

    return jsonify(course.to_dict())


# ---------------------------------------
# DELETE COURSE
# ---------------------------------------
@courses_bp.route("/<int:id>", methods=["DELETE"])
def delete_course(id):

    course = Course.query.get_or_404(id)

    db.session.delete(course)

    db.session.commit()

    return jsonify({
        "message": "Course deleted successfully"
    })


# ---------------------------------------
# GET STUDENTS ENROLLED IN A COURSE
# ---------------------------------------
@courses_bp.route("/<int:id>/students", methods=["GET"])
def get_students_in_course(id):

    course = Course.query.get_or_404(id)

    students = []

    for enrollment in course.enrollments:
        students.append(
            enrollment.student.to_dict()
        )

    return jsonify(students)


# ---------------------------------------
# GET ALL DEPARTMENTS
# ---------------------------------------
@courses_bp.route("/departments", methods=["GET"])
def get_departments():

    departments = Department.query.all()

    return jsonify(
        [dept.to_dict() for dept in departments]
    )


# ---------------------------------------
# ADD DEPARTMENT
# ---------------------------------------
@courses_bp.route("/departments", methods=["POST"])
def add_department():

    data = request.get_json()

    department = Department(
        dept_name=data["dept_name"],
        hod_name=data["hod_name"],
        budget=data["budget"]
    )

    db.session.add(department)
    db.session.commit()

    return jsonify(department.to_dict()), 201