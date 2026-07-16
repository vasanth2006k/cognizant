import { defineStore } from "pinia";
import { ref } from "vue";

import {
  getAllCourses,
  enrollStudent,
} from "../api/courseApi";

export const useCourseStore = defineStore("course", () => {

  const courses = ref([]);
  const loading = ref(false);
  const error = ref("");

  async function fetchCourses() {

    loading.value = true;
    error.value = "";

    try {
      courses.value = await getAllCourses();
    } catch (err) {
      error.value = err.message;
    } finally {
      loading.value = false;
    }
  }

  async function enroll(courseId) {

    try {
      await enrollStudent(courseId);
      alert("Student Enrolled Successfully");
    } catch (err) {
      error.value = err.message;
    }
  }

  function reset() {
    courses.value = [];
  }

  return {
    courses,
    loading,
    error,
    fetchCourses,
    enroll,
    reset,
  };
});