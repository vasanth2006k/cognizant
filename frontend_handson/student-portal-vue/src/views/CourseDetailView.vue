<template>
  <div class="container">

    <div class="card">

      <h2>{{ course.name }}</h2>

      <p><strong>Course Code:</strong> {{ course.code }}</p>

      <p><strong>Credits:</strong> {{ course.credits }}</p>

      <p><strong>Grade:</strong> {{ course.grade }}</p>

      <button @click="enrollCourse">
        Enroll
      </button>

    </div>

  </div>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router'
import { useEnrollmentStore } from '../stores/enrollment'

const route = useRoute()
const router = useRouter()
const store = useEnrollmentStore()

const courses = [
  {
    id:1,
    code:'CS101',
    name:'Programming Fundamentals',
    credits:4,
    grade:'A'
  },
  {
    id:2,
    code:'CS102',
    name:'Data Structures',
    credits:3,
    grade:'A'
  },
  {
    id:3,
    code:'CS201',
    name:'Database Management',
    credits:4,
    grade:'B+'
  },
  {
    id:4,
    code:'CS301',
    name:'Operating Systems',
    credits:4,
    grade:'A-'
  },
  {
    id:5,
    code:'CS401',
    name:'Machine Learning',
    credits:5,
    grade:'A'
  }
]

const course = courses.find(
  c => c.id == route.params.id
)

function enrollCourse() {
  store.enroll(course)
  router.push('/profile')
}
</script>