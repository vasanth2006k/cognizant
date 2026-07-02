from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import get_db
from models import Enrollment, Student, Course
from schemas import EnrollmentCreate, EnrollmentResponse

router = APIRouter(
    prefix="/api/enrollments",
    tags=["Enrollments"]
)


# -----------------------------------
# Get All Enrollments
# -----------------------------------
@router.get("/", response_model=list[EnrollmentResponse])
async def get_enrollments(db: AsyncSession = Depends(get_db)):

    result = await db.execute(select(Enrollment))

    return result.scalars().all()


# -----------------------------------
# Get Enrollment By ID
# -----------------------------------
@router.get("/{enrollment_id}", response_model=EnrollmentResponse)
async def get_enrollment(
        enrollment_id: int,
        db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(Enrollment).where(
            Enrollment.id == enrollment_id
        )
    )

    enrollment = result.scalar_one_or_none()

    if enrollment is None:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )

    return enrollment


# -----------------------------------
# Create Enrollment
# -----------------------------------
@router.post(
    "/",
    response_model=EnrollmentResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_enrollment(
        enrollment: EnrollmentCreate,
        db: AsyncSession = Depends(get_db)
):

    student = await db.get(Student, enrollment.student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    course = await db.get(Course, enrollment.course_id)

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    new_enrollment = Enrollment(
        student_id=enrollment.student_id,
        course_id=enrollment.course_id,
        enrollment_date=enrollment.enrollment_date,
        grade=enrollment.grade
    )

    db.add(new_enrollment)

    await db.commit()

    await db.refresh(new_enrollment)

    return new_enrollment


# -----------------------------------
# Delete Enrollment
# -----------------------------------
@router.delete("/{enrollment_id}")
async def delete_enrollment(
        enrollment_id: int,
        db: AsyncSession = Depends(get_db)
):

    enrollment = await db.get(
        Enrollment,
        enrollment_id
    )

    if enrollment is None:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )

    await db.delete(enrollment)

    await db.commit()

    return {
        "message": "Enrollment deleted successfully"
    }