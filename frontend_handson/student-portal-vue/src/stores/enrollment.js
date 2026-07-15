import { defineStore } from 'pinia'

export const useEnrollmentStore = defineStore('enrollment', {

  state: () => ({
    enrolledCourses: []
  }),

  getters: {

    enrolledCount(state) {
      return state.enrolledCourses.length
    },

    totalCredits(state) {
      return state.enrolledCourses.reduce(
        (total, course) => total + course.credits,
        0
      )
    }

  },

  actions: {

    enroll(course) {

      const exists = this.enrolledCourses.find(
        c => c.id === course.id
      )

      if (!exists) {
        this.enrolledCourses.push(course)
      }

    },

    unenroll(id) {

      this.enrolledCourses = this.enrolledCourses.filter(
        course => course.id !== id
      )

    }

  }

})