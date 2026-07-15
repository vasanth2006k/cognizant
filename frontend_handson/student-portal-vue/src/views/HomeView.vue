<template>
  <div class="container">

    <h1>Welcome to Student Portal</h1>

    <p>
      This Student Portal allows you to browse available courses,
      view course details, and enroll in your preferred courses.
    </p>

    <RouterLink to="/courses">
      <button>Browse Courses</button>
    </RouterLink>

  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

<style scoped>
.container{
    text-align:center;
    margin-top:60px;
}

h1{
    color:#1976d2;
    margin-bottom:20px;
}

p{
    margin-bottom:30px;
    font-size:18px;
}
</style>