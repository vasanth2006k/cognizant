import React, { useContext } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { useDispatch } from "react-redux";

import courses from "../data/courses";
import { EnrollmentContext } from "../context/EnrollmentContext";
import { enrollCourse, unenrollCourse } from "../redux/enrollmentSlice";

function CourseDetailPage() {
  const { courseId } = useParams();
  const navigate = useNavigate();
  const dispatch = useDispatch();

  const { enrolledCourses, enroll, unenroll } =
    useContext(EnrollmentContext);

  const course = courses.find(
    (c) => c.id === Number(courseId)
  );

  if (!course) {
    return (
      <div className="course-details">
        <h2>Course Not Found</h2>
        <button onClick={() => navigate("/courses")}>
          Back to Courses
        </button>
      </div>
    );
  }

  const isEnrolled = enrolledCourses.includes(course.id);

  const handleEnrollment = () => {
    if (isEnrolled) {
      unenroll(course.id);
      dispatch(unenrollCourse(course.id));
    } else {
      enroll(course.id);
      dispatch(enrollCourse(course.id));
    }
  };

  return (
    <div className="course-details">
      <h1>{course.title}</h1>

      <p>
        <strong>Instructor:</strong> {course.instructor}
      </p>

      <p>
        <strong>Duration:</strong> {course.duration}
      </p>

      <p>
        <strong>Level:</strong> {course.level}
      </p>

      <p>
        <strong>Description:</strong>
      </p>

      <p>{course.description}</p>

      <button
        className="enroll-btn"
        onClick={handleEnrollment}
      >
        {isEnrolled ? "Unenroll" : "Enroll"}
      </button>

      <button
        className="back-btn"
        onClick={() => navigate("/courses")}
      >
        Back to Courses
      </button>
    </div>
  );
}

export default CourseDetailPage;