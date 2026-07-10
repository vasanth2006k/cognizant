import React from "react";
import { Routes, Route } from "react-router-dom";

import Header from "./components/Header";
import HomePage from "./pages/HomePage";
import CoursesPage from "./pages/CoursesPage";
import CourseDetailPage from "./pages/CourseDetailPage";
import ProfilePage from "./pages/ProfilePage";

import "./App.css";

function App() {
  return (
    <div className="app">
      <Header />

      <div className="container">
        <Routes>
          <Route path="/" element={<HomePage />} />

          <Route path="/courses" element={<CoursesPage />} />

          <Route
            path="/courses/:courseId"
            element={<CourseDetailPage />}
          />

          <Route path="/profile" element={<ProfilePage />} />
        </Routes>
      </div>
    </div>
  );
}

export default App;