from fastapi import FastAPI
from schemas import CourseCreate

app = FastAPI(
    title="Course Management API",
    version="1.0"
)


@app.get("/")
async def home():
    return {"message": "API running"}


@app.post("/api/courses/")
async def create_course(course: CourseCreate):

    return {
        "message": "Course Created",
        "course": course
    }