import React from "react";
import CourseCard from "../components/CourseCard";
import courses from "../data/courses";

function CoursesPage() {
  return (
    <div className="courses-page">
      <h1>Available Courses</h1>

      <div className="courses-grid">
        {courses.map((course) => (
          <CourseCard key={course.id} course={course} />
        ))}
      </div>
    </div>
  );
}

export default CoursesPage;