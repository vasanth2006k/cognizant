from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, or_

from database import get_db
from models import Course
from schemas import CourseCreate, CourseUpdate, CourseResponse

router = APIRouter(
    prefix="/api/v1/courses",
    tags=["Courses"]
)


# -----------------------------
# GET ALL COURSES
# Pagination + Search
# -----------------------------
@router.get("/")
async def get_courses(
    page: int = 1,
    page_size: int = 2,
    search: str | None = None,
    db: AsyncSession = Depends(get_db)
):

    query = select(Course)

    if search:
        query = query.where(
            or_(
                Course.course_name.ilike(f"%{search}%"),
                Course.course_code.ilike(f"%{search}%")
            )
        )

    total = len(
        (
            await db.execute(query)
        ).scalars().all()
    )

    offset = (page - 1) * page_size

    result = await db.execute(
        query.offset(offset).limit(page_size)
    )

    courses = result.scalars().all()

    next_page = None
    previous_page = None

    if offset + page_size < total:
        next_page = f"/api/v1/courses?page={page+1}&page_size={page_size}"

    if page > 1:
        previous_page = f"/api/v1/courses?page={page-1}&page_size={page_size}"

    return {
        "count": total,
        "next": next_page,
        "previous": previous_page,
        "results": courses
    }


# -----------------------------
# GET COURSE BY ID
# -----------------------------
@router.get(
    "/{course_id}",
    response_model=CourseResponse
)
async def get_course(
    course_id: int,
    db: AsyncSession = Depends(get_db)
):

    course = await db.get(Course, course_id)

    if course is None:
        raise HTTPException(
            status_code=404,
            detail={
                "error": {
                    "code": "NOT_FOUND",
                    "message": f"Course with id {course_id} does not exist",
                    "field": None
                }
            }
        )

    return course


# -----------------------------
# CREATE COURSE
# -----------------------------
@router.post(
    "/",
    response_model=CourseResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_course(
    course: CourseCreate,
    response: Response,
    db: AsyncSession = Depends(get_db)
):

    new_course = Course(
        course_name=course.course_name,
        course_code=course.course_code,
        credits=course.credits,
        department_id=course.department_id
    )

    db.add(new_course)

    await db.commit()

    await db.refresh(new_course)

    response.headers["Location"] = f"/api/v1/courses/{new_course.id}"

    return new_course


# -----------------------------
# PUT
# Replace entire object
# -----------------------------
@router.put(
    "/{course_id}",
    response_model=CourseResponse
)
async def update_course(
    course_id: int,
    course: CourseCreate,
    db: AsyncSession = Depends(get_db)
):

    db_course = await db.get(Course, course_id)

    if db_course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    db_course.course_name = course.course_name
    db_course.course_code = course.course_code
    db_course.credits = course.credits
    db_course.department_id = course.department_id

    await db.commit()

    await db.refresh(db_course)

    return db_course


# -----------------------------
# PATCH
# Partial Update
# -----------------------------
@router.patch(
    "/{course_id}",
    response_model=CourseResponse
)
async def patch_course(
    course_id: int,
    course: CourseUpdate,
    db: AsyncSession = Depends(get_db)
):

    db_course = await db.get(Course, course_id)

    if db_course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    update_data = course.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_course, key, value)

    await db.commit()

    await db.refresh(db_course)

    return db_course


# -----------------------------
# DELETE
# -----------------------------
@router.delete(
    "/{course_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_course(
    course_id: int,
    db: AsyncSession = Depends(get_db)
):

    course = await db.get(Course, course_id)

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    await db.delete(course)

    await db.commit()

    return None