import { useEffect, useState } from "react";

import Header from "./components/Header";
import Footer from "./components/Footer";
import CourseCard from "./components/CourseCard";
import StudentProfile from "./components/StudentProfile";

import coursesData from "./data/courses";

function App() {

    const [courses, setCourses] = useState([]);

    const [loading, setLoading] = useState(true);

    const [error, setError] = useState("");

    const [searchTerm, setSearchTerm] = useState("");

    const [enrolledCourses, setEnrolledCourses] = useState([]);

    useEffect(() => {

        try{

            setTimeout(()=>{

                setCourses(coursesData);

                setLoading(false);

            },1000);

        }

        catch{

            setError("Unable to load courses");

            setLoading(false);

        }

    },[]);

    useEffect(()=>{

        console.log("Courses Updated");

    },[courses]);

    function handleEnroll(id){

        if(!enrolledCourses.includes(id)){

            setEnrolledCourses([...enrolledCourses,id]);

        }

    }

    const filteredCourses = courses.filter(course=>{

        return course.name.toLowerCase().includes(searchTerm.toLowerCase());

    });

    return(

        <>

        <Header
        siteName="Student Portal"
        enrolledCount={enrolledCourses.length}
        />

        <div className="container">

            <input

            type="text"

            placeholder="Search Course"

            value={searchTerm}

            onChange={(e)=>setSearchTerm(e.target.value)}

            className="search"

            />

            {loading && <h2>Loading...</h2>}

            {error && <h2>{error}</h2>}

            <div className="grid">

            {

                filteredCourses.map(course=>(

                    <CourseCard

                    key={course.id}

                    id={course.id}

                    name={course.name}

                    code={course.code}

                    credits={course.credits}

                    grade={course.grade}

                    onEnroll={handleEnroll}

                    />

                ))

            }

            </div>

            <StudentProfile/>

        </div>

        <Footer/>

        </>

    );

}

export default App;