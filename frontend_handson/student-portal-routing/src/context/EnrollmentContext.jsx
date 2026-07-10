import React, { createContext, useState } from "react";
export const EnrollmentContext = createContext();

export const EnrollmentProvider = ({ children }) => {
  const [enrolledCourses, setEnrolledCourses] = useState([]);

  const enroll = (courseId) => {
    if (!enrolledCourses.includes(courseId)) {
      setEnrolledCourses([...enrolledCourses, courseId]);
    }
  };

  const unenroll = (courseId) => {
    setEnrolledCourses(
      enrolledCourses.filter((id) => id !== courseId)
    );
  };

  return (
    <EnrollmentContext.Provider
      value={{
        enrolledCourses,
        enroll,
        unenroll,
      }}
    >
      {children}
    </EnrollmentContext.Provider>
  );
};