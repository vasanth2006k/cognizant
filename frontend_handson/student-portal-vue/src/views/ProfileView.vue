<template>
  <div class="container">

    <h2>My Profile</h2>

    <h3>Enrolled Courses</h3>

    <div
      class="card"
      v-for="course in store.enrolledCourses"
      :key="course.id"
    >
      <h3>{{ course.name }}</h3>

      <p>{{ course.code }}</p>

      <p>Credits : {{ course.credits }}</p>

      <button
        @click="store.unenroll(course.id)"
      >
        Unenroll
      </button>
    </div>

    <h2>Total Credits : {{ store.totalCredits }}</h2>

  </div>
</template>

<script setup>
import { useEnrollmentStore } from '../stores/enrollment'

const store = useEnrollmentStore()
</script>