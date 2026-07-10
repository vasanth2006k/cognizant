import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  enrolledCourses: [],
};

const enrollmentSlice = createSlice({
  name: "enrollment",
  initialState,
  reducers: {
    enrollCourse: (state, action) => {
      if (!state.enrolledCourses.includes(action.payload)) {
        state.enrolledCourses.push(action.payload);
      }
    },

    unenrollCourse: (state, action) => {
      state.enrolledCourses = state.enrolledCourses.filter(
        (id) => id !== action.payload
      );
    },
  },
});

export const { enrollCourse, unenrollCourse } =
  enrollmentSlice.actions;

export default enrollmentSlice.reducer;