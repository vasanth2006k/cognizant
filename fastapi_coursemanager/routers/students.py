from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import get_db
from models import Student
from schemas import StudentCreate, StudentUpdate, StudentResponse

router = APIRouter(
    prefix="/api/students",
    tags=["Students"]
)


# ------------------------------------
# Get All Students
# ------------------------------------
@router.get("/", response_model=list[StudentResponse])
async def get_students(db: AsyncSession = Depends(get_db)):

    result = await db.execute(select(Student))

    return result.scalars().all()


# ------------------------------------
# Get Student By ID
# ------------------------------------
@router.get("/{student_id}", response_model=StudentResponse)
async def get_student(student_id: int,
                      db: AsyncSession = Depends(get_db)):

    result = await db.execute(
        select(Student).where(Student.id == student_id)
    )

    student = result.scalar_one_or_none()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


# ------------------------------------
# Add Student
# ------------------------------------
@router.post(
    "/",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_student(student: StudentCreate,
                         db: AsyncSession = Depends(get_db)):

    new_student = Student(
        first_name=student.first_name,
        last_name=student.last_name,
        email=student.email,
        enrollment_year=student.enrollment_year,
        department_id=student.department_id
    )

    db.add(new_student)

    await db.commit()

    await db.refresh(new_student)

    return new_student


# ------------------------------------
# Update Student
# ------------------------------------
@router.put("/{student_id}",
            response_model=StudentResponse)
async def update_student(student_id: int,
                         data: StudentUpdate,
                         db: AsyncSession = Depends(get_db)):

    result = await db.execute(
        select(Student).where(Student.id == student_id)
    )

    student = result.scalar_one_or_none()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    update_data = data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(student, key, value)

    await db.commit()

    await db.refresh(student)

    return student


# ------------------------------------
# Delete Student
# ------------------------------------
@router.delete("/{student_id}")
async def delete_student(student_id: int,
                         db: AsyncSession = Depends(get_db)):

    result = await db.execute(
        select(Student).where(Student.id == student_id)
    )

    student = result.scalar_one_or_none()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    await db.delete(student)

    await db.commit()

    return {
        "message": "Student deleted successfully"
    }