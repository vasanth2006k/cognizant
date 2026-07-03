from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from models import Enrollment
from schemas import EnrollmentCreate, EnrollmentResponse
from security import get_current_user

router = APIRouter(
    prefix="/api/v1/enrollments",
    tags=["Enrollments"]
)


# ======================================
# GET ALL ENROLLMENTS (Public)
# ======================================
@router.get("/", response_model=list[EnrollmentResponse])
def get_enrollments(db: Session = Depends(get_db)):
    return db.query(Enrollment).all()


# ======================================
# GET ENROLLMENT BY ID (Public)
# ======================================
@router.get("/{enrollment_id}", response_model=EnrollmentResponse)
def get_enrollment(
    enrollment_id: int,
    db: Session = Depends(get_db)
):

    enrollment = db.query(Enrollment).filter(
        Enrollment.id == enrollment_id
    ).first()

    if enrollment is None:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )

    return enrollment


# ======================================
# CREATE ENROLLMENT (Protected)
# ======================================
@router.post(
    "/",
    response_model=EnrollmentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_enrollment(
    enrollment: EnrollmentCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    new_enrollment = Enrollment(
        student_id=enrollment.student_id,
        course_id=enrollment.course_id,
        enrollment_date=enrollment.enrollment_date,
        grade=enrollment.grade
    )

    db.add(new_enrollment)
    db.commit()
    db.refresh(new_enrollment)

    return new_enrollment


# ======================================
# UPDATE ENROLLMENT (Protected)
# ======================================
@router.put("/{enrollment_id}", response_model=EnrollmentResponse)
def update_enrollment(
    enrollment_id: int,
    enrollment_data: EnrollmentCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    enrollment = db.query(Enrollment).filter(
        Enrollment.id == enrollment_id
    ).first()

    if enrollment is None:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )

    enrollment.student_id = enrollment_data.student_id
    enrollment.course_id = enrollment_data.course_id
    enrollment.enrollment_date = enrollment_data.enrollment_date
    enrollment.grade = enrollment_data.grade

    db.commit()
    db.refresh(enrollment)

    return enrollment


# ======================================
# DELETE ENROLLMENT (Protected)
# ======================================
@router.delete("/{enrollment_id}")
def delete_enrollment(
    enrollment_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    enrollment = db.query(Enrollment).filter(
        Enrollment.id == enrollment_id
    ).first()

    if enrollment is None:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )

    db.delete(enrollment)
    db.commit()

    return {
        "message": "Enrollment deleted successfully"
    }