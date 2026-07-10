import React from "react";
import { useNavigate } from "react-router-dom";

function HomePage() {
  const navigate = useNavigate();

  return (
    <div className="home-page">
      <h1>Welcome to the Student Course Portal</h1>

      <p>
        Explore a wide range of courses, view detailed information,
        and manage your enrollments easily.
      </p>

      <button
        className="explore-btn"
        onClick={() => navigate("/courses")}
      >
        Explore Courses
      </button>
    </div>
  );
}

export default HomePage;