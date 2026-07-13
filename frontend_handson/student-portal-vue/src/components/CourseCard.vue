<template>
  <div class="card">
    <h3>{{ course.name }}</h3>

    <p><strong>Code:</strong> {{ course.code }}</p>

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
  course: Object
})
</script>

<style scoped>
.card{
    background:white;
    margin:20px;
    padding:20px;
    border-radius:10px;
    box-shadow:0 0 10px rgba(0,0,0,.15);
}
</style>