<template>
  <div class="container">

    <h1>Available Courses</h1>

    <input
      type="text"
      v-model="search"
      placeholder="Search Course..."
    />

    <CourseCard
      v-for="course in filteredCourses"
      :key="course.id"
      :course="course"
    />

  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import CourseCard from '../components/CourseCard.vue'

const search = ref('')

const courses = ref([
  {
    id: 1,
    code: 'CS101',
    name: 'Programming Fundamentals',
    credits: 4,
    grade: 'A'
  },
  {
    id: 2,
    code: 'CS102',
    name: 'Data Structures',
    credits: 3,
    grade: 'A'
  },
  {
    id: 3,
    code: 'CS201',
    name: 'Database Management',
    credits: 4,
    grade: 'B+'
  },
  {
    id: 4,
    code: 'CS301',
    name: 'Operating Systems',
    credits: 4,
    grade: 'A-'
  },
  {
    id: 5,
    code: 'CS401',
    name: 'Machine Learning',
    credits: 5,
    grade: 'A'
  }
])

const filteredCourses = computed(() => {
  return courses.value.filter(course =>
    course.name.toLowerCase().includes(search.value.toLowerCase())
  )
})
</script>

<style scoped>
h1{
    text-align:center;
    margin-bottom:20px;
    color:#1976d2;
}

input{
    margin-bottom:20px;
}
</style>