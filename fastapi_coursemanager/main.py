from fastapi import FastAPI

from database import Base, engine

# Import models so SQLAlchemy registers all tables
import models

# Create all tables
Base.metadata.create_all(bind=engine)

# Import routers
from routers.auth import router as auth_router
from routers.courses import router as course_router
from routers.students import router as student_router
from routers.enrollments import router as enrollment_router

app = FastAPI(
    title="Course Management API",
    version="1.0.0"
)

# Register routers
app.include_router(auth_router)
app.include_router(course_router)
app.include_router(student_router)
app.include_router(enrollment_router)


@app.get("/")
def root():
    return {
        "message": "Course Management API is running"
    }