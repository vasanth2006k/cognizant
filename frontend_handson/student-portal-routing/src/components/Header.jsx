import React from "react";

import { Link, useLocation } from "react-router-dom";
import "./Header.css";

function Header() {
  const location = useLocation();

  return (
    <header className="header">
      <div className="logo">
        <h2>🎓 Student Portal</h2>
      </div>

      <nav>
        <ul className="nav-links">
          <li>
            <Link
              to="/"
              className={location.pathname === "/" ? "active" : ""}
            >
              Home
            </Link>
          </li>

          <li>
            <Link
              to="/courses"
              className={
                location.pathname.startsWith("/courses") ? "active" : ""
              }
            >
              Courses
            </Link>
          </li>

          <li>
            <Link
              to="/profile"
              className={location.pathname === "/profile" ? "active" : ""}
            >
              Profile
            </Link>
          </li>
        </ul>
      </nav>
    </header>
  );
}

export default Header;