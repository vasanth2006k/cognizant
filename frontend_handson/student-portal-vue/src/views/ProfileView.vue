<template>
  <div class="container">

    <h1>My Profile</h1>

    <div v-if="store.enrolledCourses.length === 0">
      <p>No courses enrolled yet.</p>
    </div>

    <div
      v-for="course in store.enrolledCourses"
      :key="course.id"
      class="card"
    >
      <h2>{{ course.name }}</h2>

      <p><strong>Course Code:</strong> {{ course.code }}</p>

      <p><strong>Credits:</strong> {{ course.credits }}</p>

      <p><strong>Grade:</strong> {{ course.grade }}</p>

      <button @click="store.unenroll(course.id)">
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

<style scoped>
h1{
    text-align:center;
    color:#1976d2;
    margin-bottom:20px;
}

.card{
    margin-bottom:20px;
}

button{
    margin-top:10px;
}
</style>