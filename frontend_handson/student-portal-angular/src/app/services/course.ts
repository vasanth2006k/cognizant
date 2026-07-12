import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CourseService {

  private http = inject(HttpClient);

  getCourses(): Observable<any[]> {
    return this.http.get<any[]>(
      'https://jsonplaceholder.typicode.com/posts?_limit=5'
    );
  }

}