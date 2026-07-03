from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from models import Course
from schemas import CourseCreate, CourseUpdate, CourseResponse
from security import get_current_user

router = APIRouter(
    prefix="/api/v1/courses",
    tags=["Courses"]
)


# =====================================
# GET ALL COURSES (Public)
# =====================================
@router.get("/", response_model=list[CourseResponse])
def get_courses(db: Session = Depends(get_db)):
    return db.query(Course).all()


# =====================================
# GET COURSE BY ID (Public)
# =====================================
@router.get("/{course_id}", response_model=CourseResponse)
def get_course(course_id: int, db: Session = Depends(get_db)):

    course = db.query(Course).filter(
        Course.id == course_id
    ).first()

    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return course


# =====================================
# CREATE COURSE (Protected)
# =====================================
@router.post(
    "/",
    response_model=CourseResponse,
    status_code=status.HTTP_201_CREATED
)
def create_course(
    course: CourseCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    new_course = Course(
        course_name=course.course_name,
        course_code=course.course_code,
        credits=course.credits,
        department_id=course.department_id
    )

    db.add(new_course)
    db.commit()
    db.refresh(new_course)

    return new_course


# =====================================
# UPDATE COURSE (Protected)
# =====================================
@router.put("/{course_id}", response_model=CourseResponse)
def update_course(
    course_id: int,
    updated_course: CourseUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    course = db.query(Course).filter(
        Course.id == course_id
    ).first()

    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    update_data = updated_course.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(course, key, value)

    db.commit()
    db.refresh(course)

    return course


# =====================================
# DELETE COURSE (Protected)
# =====================================
@router.delete("/{course_id}")
def delete_course(
    course_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    course = db.query(Course).filter(
        Course.id == course_id
    ).first()

    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    db.delete(course)
    db.commit()

    return {
        "message": "Course deleted successfully"
    }