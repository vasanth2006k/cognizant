<template>
  <div class="container">
    <h1>Welcome to Student Portal</h1>

    <p>
      This application allows students to browse courses, view details,
      and enroll in courses using Vue Router and Pinia.
    </p>

    <RouterLink to="/courses">
      <button>Browse Courses</button>
    </RouterLink>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>