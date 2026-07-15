<template>
  <div class="card">

    <h2>{{ course.name }}</h2>

    <p><strong>Course Code:</strong> {{ course.code }}</p>

    <p><strong>Credits:</strong> {{ course.credits }}</p>

    <p><strong>Grade:</strong> {{ course.grade }}</p>

    <RouterLink :to="'/course/' + course.id">
      <button>View Details</button>
    </RouterLink>

  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'

defineProps({
  course: {
    type: Object,
    required: true
  }
})
</script>

<style scoped>
.card{
    background:white;
    padding:20px;
    margin:20px 0;
    border-radius:10px;
    box-shadow:0 2px 8px rgba(0,0,0,0.15);
}

button{
    margin-top:15px;
}
</style>