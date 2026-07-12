import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { CourseCardComponent } from '../course-card/course-card';
import { CourseService } from '../services/course';
@Component({
  selector: 'app-course-list',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    CourseCardComponent
  ],
  templateUrl: './course-list.html',
  styleUrl: './course-list.css'
})
export class CourseListComponent implements OnInit {

  private courseService = inject(CourseService);

  courses: any[] = [];
  filteredCourses: any[] = [];

  searchTerm = '';

  loading = false;

  ngOnInit(): void {

    this.loading = true;

    this.courseService.getCourses().subscribe({

      next: (data) => {

      const courseNames = [
  'Data Structures',
  'Database Management Systems',
  'Operating Systems',
  'Computer Networks',
  'Software Engineering'
];

this.courses = data.map((course, index) => ({
  name: courseNames[index] || `Course ${index + 1}`,
  code: `CS10${index + 1}`,
  credits: 4,
  grade: 'A'
}));

        this.filteredCourses = this.courses;

        this.loading = false;
      },

      error: () => {
        this.loading = false;
      }

    });

  }

  searchCourse() {

    this.filteredCourses = this.courses.filter(course =>
      course.name.toLowerCase().includes(this.searchTerm.toLowerCase())
    );

  }

}