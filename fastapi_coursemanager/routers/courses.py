from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from fastapi import BackgroundTasks

from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db

from schemas import (
    CourseCreate,
    CourseUpdate,
    CourseResponse
)

import crud

router = APIRouter(
    prefix="/api/courses",
    tags=["Courses"]
)


def send_confirmation_email(email: str):
    print(f"Sending confirmation to {email}")


@router.get(
    "/",
    response_model=list[CourseResponse]
)
async def get_all_courses(
        db: AsyncSession = Depends(get_db)
):

    return await crud.get_courses(db)


@router.get(
    "/{course_id}",
    response_model=CourseResponse
)
async def get_course(
        course_id: int,
        db: AsyncSession = Depends(get_db)
):

    course = await crud.get_course(
        db,
        course_id
    )

    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return course


@router.post(
    "/",
    response_model=CourseResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create Course",
    response_description="New course created"
)
async def create_course(
        course: CourseCreate,
        background_tasks: BackgroundTasks,
        db: AsyncSession = Depends(get_db)
):

    new_course = await crud.create_course(
        db,
        course
    )

    background_tasks.add_task(
        send_confirmation_email,
        "student@example.com"
    )

    return new_course


@router.put(
    "/{course_id}",
    response_model=CourseResponse
)
async def update_course(
        course_id: int,
        course: CourseUpdate,
        db: AsyncSession = Depends(get_db)
):

    updated = await crud.update_course(
        db,
        course_id,
        course
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return updated


@router.delete(
    "/{course_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_course(
        course_id: int,
        db: AsyncSession = Depends(get_db)
):

    deleted = await crud.delete_course(
        db,
        course_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return