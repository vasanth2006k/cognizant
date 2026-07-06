import { courses } from "./data.js";

// ES6 Map
const courseNames = courses.map(
    ({code,name,credits}) =>
    `${code} - ${name} (${credits} credits)`
);

console.log(courseNames);

// Filter

const filteredCourses =
courses.filter(course => course.credits >=4);

console.log(filteredCourses);

// Reduce

const totalCredits =
courses.reduce(
    (sum,course)=>sum+course.credits,
    0
);

console.log(totalCredits);

const courseGrid =
document.querySelector(".course-grid");

const total =
document.querySelector("#total-credits");

const selected =
document.querySelector("#selected-course");

function displayCourses(list){

    courseGrid.innerHTML="";

    list.forEach(course=>{

        const article=
        document.createElement("article");

        article.className="course-card";

        article.dataset.id=course.id;

        article.innerHTML=`

            <h3>${course.name}</h3>

            <p>${course.code}</p>

            <span>${course.credits} Credits</span>

        `;

        courseGrid.appendChild(article);

    });

    total.textContent=
    `Total Credits : ${
        list.reduce((sum,c)=>sum+c.credits,0)
    }`;

}

displayCourses(courses);

// Search

const searchBox=
document.querySelector("#search-courses");

searchBox.addEventListener("input",()=>{

    const keyword=
    searchBox.value.toLowerCase();

    const result=
    courses.filter(course=>

        course.name
        .toLowerCase()
        .includes(keyword)

    );

    displayCourses(result);

});

// Sort

document
.getElementById("sortBtn")
.addEventListener("click",()=>{

    const sorted=
    [...courses].sort(

        (a,b)=>b.credits-a.credits

    );

    displayCourses(sorted);

});

// Event Delegation

courseGrid.addEventListener("click",(e)=>{

    const card=
    e.target.closest(".course-card");

    if(!card)
        return;

    const id=
    Number(card.dataset.id);

    const course=
    courses.find(c=>c.id===id);

    selected.innerHTML=`

        <h2>${course.name}</h2>

        <p>Grade : ${course.grade}</p>

    `;

});