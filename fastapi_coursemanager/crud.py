from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import Course
from schemas import CourseCreate, CourseUpdate


async def get_courses(db: AsyncSession):

    result = await db.execute(select(Course))

    return result.scalars().all()


async def get_course(db: AsyncSession, course_id: int):

    result = await db.execute(
        select(Course).where(
            Course.id == course_id
        )
    )

    return result.scalar_one_or_none()


async def create_course(db: AsyncSession, course: CourseCreate):

    new_course = Course(
        course_name=course.course_name,
        course_code=course.course_code,
        credits=course.credits,
        department_id=course.department_id
    )

    db.add(new_course)

    await db.commit()

    await db.refresh(new_course)

    return new_course


async def update_course(
        db: AsyncSession,
        course_id: int,
        data: CourseUpdate
):

    course = await get_course(db, course_id)

    if not course:
        return None

    update_data = data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(course, key, value)

    await db.commit()

    await db.refresh(course)

    return course


async def delete_course(
        db: AsyncSession,
        course_id: int
):

    course = await get_course(db, course_id)

    if not course:
        return False

    await db.delete(course)

    await db.commit()

    return True