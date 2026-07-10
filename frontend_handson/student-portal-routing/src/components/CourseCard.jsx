import React from "react";
import { useNavigate } from "react-router-dom";

function CourseCard({ course }) {
  const navigate = useNavigate();

  const handleViewDetails = () => {
    navigate(`/courses/${course.id}`);
  };

  return (
    <div className="course-card">
      <h2>{course.title}</h2>

      <p>
        <strong>Instructor:</strong> {course.instructor}
      </p>

      <p>
        <strong>Duration:</strong> {course.duration}
      </p>

      <p>
        <strong>Level:</strong> {course.level}
      </p>

      <button
        className="details-btn"
        onClick={handleViewDetails}
      >
        View Details
      </button>
    </div>
  );
}

export default CourseCard;