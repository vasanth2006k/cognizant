<template>
  <div class="page">

    <header class="hero">
      <h1>📚 Online Course Portal</h1>
      <p>Learn New Skills Anytime, Anywhere</p>

      <div class="buttons">
        <button @click="loadCourses">Load Courses</button>
        <button class="reset" @click="resetCourses">Reset</button>
      </div>
    </header>

    <div class="course-grid">

      <div
        class="course-card"
        v-for="course in courses"
        :key="course.id"
      >

        <div class="icon">🎓</div>

        <h2>{{ course.title }}</h2>

        <p>{{ course.body }}</p>

        <div class="details">

          <span>⏱ 8 Weeks</span>

          <span>⭐ Beginner</span>

        </div>

        <div class="footer">

          <h3>₹4,999</h3>

          <button @click="enroll(course.id)">
            Enroll Now
          </button>

        </div>

      </div>

    </div>

  </div>
</template>

<script setup>

import { storeToRefs } from "pinia";
import { useCourseStore } from "../stores/courseStore";

const store = useCourseStore();

const { courses } = storeToRefs(store);

const { fetchCourses, reset, enroll } = store;

const loadCourses = () => fetchCourses();

const resetCourses = () => reset();

</script>

<style scoped>

*{
margin:0;
padding:0;
box-sizing:border-box;
font-family:'Segoe UI',sans-serif;
}

.page{

min-height:100vh;

background:#eef3f8;

padding-bottom:50px;

}

.hero{

background:linear-gradient(135deg,#1565C0,#42A5F5);

padding:50px;

color:white;

text-align:center;

}

.hero h1{

font-size:45px;

margin-bottom:10px;

}

.hero p{

font-size:20px;

margin-bottom:25px;

}

.buttons button{

margin:10px;

padding:12px 25px;

border:none;

border-radius:30px;

cursor:pointer;

font-size:16px;

background:white;

color:#1565C0;

font-weight:bold;

transition:.3s;

}

.buttons button:hover{

transform:scale(1.05);

}

.reset{

background:#ff5252!important;

color:white!important;

}

.course-grid{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(320px,1fr));

gap:30px;

padding:40px;

}

.course-card{

background:white;

border-radius:20px;

padding:25px;

box-shadow:0 10px 30px rgba(0,0,0,.15);

transition:.4s;

}

.course-card:hover{

transform:translateY(-10px);

}

.icon{

font-size:55px;

margin-bottom:15px;

}

.course-card h2{

color:#1565C0;

margin-bottom:15px;

}

.course-card p{

color:#666;

line-height:1.7;

margin-bottom:20px;

}

.details{

display:flex;

justify-content:space-between;

margin-bottom:20px;

font-size:15px;

color:#555;

}

.footer{

display:flex;

justify-content:space-between;

align-items:center;

}

.footer h3{

color:#2E7D32;

}

.footer button{

background:#1565C0;

color:white;

padding:10px 20px;

border:none;

border-radius:30px;

cursor:pointer;

font-weight:bold;

transition:.3s;

}

.footer button:hover{

background:#0D47A1;

}

</style>