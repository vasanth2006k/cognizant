import React, { useContext } from "react";
import { useSelector } from "react-redux";

import { EnrollmentContext } from "../context/EnrollmentContext";
import courses from "../data/courses";
function ProfilePage() {
  const { enrolledCourses } = useContext(EnrollmentContext);

  const reduxEnrolledCourses = useSelector(
    (state) => state.enrollment.enrolledCourses
  );

  const myCourses = courses.filter((course) =>
    enrolledCourses.includes(course.id)
  );

  return (
    <div className="profile-page">
      <h1>Student Profile</h1>

      <div className="profile-card">
        <h2>John Doe</h2>
        <p>Email: john@example.com</p>
        <p>Role: Student</p>
      </div>

      <div className="enrolled-section">
        <h2>My Enrolled Courses</h2>

        {myCourses.length === 0 ? (
          <p>No courses enrolled yet.</p>
        ) : (
          <div className="courses-grid">
            {myCourses.map((course) => (
              <div key={course.id} className="course-card">
                <h3>{course.title}</h3>

                <p>
                  <strong>Instructor:</strong>{" "}
                  {course.instructor}
                </p>

                <p>
                  <strong>Duration:</strong>{" "}
                  {course.duration}
                </p>

                <p>
                  <strong>Level:</strong>{" "}
                  {course.level}
                </p>
              </div>
            ))}
          </div>
        )}

        <div className="redux-info">
          <h3>Redux Store</h3>
          <p>
            Enrolled Course IDs:{" "}
            {reduxEnrolledCourses.length > 0
              ? reduxEnrolledCourses.join(", ")
              : "None"}
          </p>
        </div>
      </div>
    </div>
  );
}

export default ProfilePage;