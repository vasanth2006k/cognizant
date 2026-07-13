import { defineStore } from 'pinia'

export const useEnrollmentStore = defineStore('enrollment', {

    state: () => ({
        enrolledCourses: []
    }),

    getters: {

        totalCredits(state) {
            return state.enrolledCourses.reduce(
                (total, course) => total + course.credits,
                0
            )
        },

        enrolledCount(state) {
            return state.enrolledCourses.length
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
            this.enrolledCourses =
                this.enrolledCourses.filter(
                    c => c.id !== id
                )
        }
    }

})