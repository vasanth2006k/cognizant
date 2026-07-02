from fastapi import FastAPI

from database import Base
from database import engine

from routers.courses import router as course_router
from routers.students import router as student_router
from routers.enrollments import router as enrollment_router

app = FastAPI(
    title="Course Management API",
    version="1.0"
)


@app.on_event("startup")
async def startup():

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


app.include_router(course_router)
app.include_router(student_router)
app.include_router(enrollment_router)