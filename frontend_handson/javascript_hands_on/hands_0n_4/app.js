// -------------------------------
// DOM Elements
// -------------------------------

const courseGrid = document.querySelector(".course-grid");
const notifications = document.getElementById("notifications");

const loading = document.getElementById("loading");
const error = document.getElementById("error");

const retryBtn = document.getElementById("retryBtn");

const searchInput = document.getElementById("search-courses");
const sortBtn = document.getElementById("sortBtn");

const totalCredits = document.getElementById("total-credits");
const selectedCourse = document.getElementById("selected-course");

// -------------------------------
// Global Courses Array
// -------------------------------

let currentCourses = [];

// -------------------------------
// Simulated API
// -------------------------------

function fetchAllCourses() {

    return new Promise((resolve) => {

        setTimeout(() => {

            resolve([

                {
                    id: 1,
                    name: "Data Structures",
                    code: "CS201",
                    credits: 4,
                    grade: "A"
                },

                {
                    id: 2,
                    name: "DBMS",
                    code: "CS202",
                    credits: 3,
                    grade: "A+"
                },

                {
                    id: 3,
                    name: "Operating System",
                    code: "CS203",
                    credits: 4,
                    grade: "B+"
                }

            ]);

        },1000);

    });

}

// -------------------------------
// Render Courses
// -------------------------------

function renderCourses(courses){

    courseGrid.innerHTML="";

    courses.forEach(course=>{

        const card=document.createElement("div");

        card.className="course-card";

        card.dataset.id=course.id;

        card.innerHTML=`

            <h3>${course.name}</h3>

            <p>${course.code}</p>

            <span>${course.credits} Credits</span>

        `;

        courseGrid.appendChild(card);

    });

    const credits=courses.reduce((sum,course)=>{

        return sum+course.credits;

    },0);

    totalCredits.textContent=
    "Total Credits : "+credits;

}

// -------------------------------
// Load Courses
// -------------------------------

async function loadCourses(){

    loading.textContent="Loading Courses...";

    currentCourses=await fetchAllCourses();

    loading.textContent="";

    renderCourses(currentCourses);

}

loadCourses();

// -------------------------------
// Click Course Card (Hands-On 3)
// -------------------------------

courseGrid.addEventListener("click", (event) => {

    const card = event.target.closest(".course-card");

    if (!card) return;

    const id = Number(card.dataset.id);

    const course = currentCourses.find(c => c.id === id);

    selectedCourse.innerHTML = `
        <h2>${course.name}</h2>
        <p><strong>Course Code:</strong> ${course.code}</p>
        <p><strong>Credits:</strong> ${course.credits}</p>
        <p><strong>Grade:</strong> ${course.grade}</p>
    `;

});


// -------------------------------
// Search Courses
// -------------------------------

searchInput.addEventListener("input", () => {

    const keyword = searchInput.value.toLowerCase();

    const filteredCourses = currentCourses.filter(course =>

        course.name.toLowerCase().includes(keyword) ||
        course.code.toLowerCase().includes(keyword)

    );

    renderCourses(filteredCourses);

});


// -------------------------------
// Sort Courses by Credits
// -------------------------------

sortBtn.addEventListener("click", () => {

    const sortedCourses = [...currentCourses].sort(

        (a, b) => b.credits - a.credits

    );

    renderCourses(sortedCourses);

});


// -------------------------------
// Promise Example (.then())
// -------------------------------

function fetchUser(id) {

    return fetch(
        "https://jsonplaceholder.typicode.com/users/" + id
    );

}

fetchUser(1)
    .then(response => response.json())
    .then(data => {

        console.log("User 1:", data.name);

    });


// -------------------------------
// Async/Await Example
// -------------------------------

async function fetchUserAsync(id) {

    try {

        const response = await fetch(
            "https://jsonplaceholder.typicode.com/users/" + id
        );

        const data = await response.json();

        console.log("User", id + ":", data.name);

    }

    catch (error) {

        console.log(error);

    }

}

fetchUserAsync(2);


// -------------------------------
// Promise.all()
// -------------------------------

Promise.all([

    fetchUserAsync(1),

    fetchUserAsync(2)

]).then(() => {

    console.log("Both users loaded.");

});
// ------------------------------------
// Generic Fetch Function
// ------------------------------------

async function apiFetch(url) {

    const response = await fetch(url);

    if (!response.ok) {

        throw new Error("Failed to fetch data.");

    }

    return await response.json();

}


// ------------------------------------
// Load Notifications
// ------------------------------------

async function loadNotifications() {

    try {

        loading.textContent = "Loading Notifications...";

        error.textContent = "";

        retryBtn.style.display = "none";

        const posts = await apiFetch(
            "https://jsonplaceholder.typicode.com/posts?_limit=5"
        );

        loading.textContent = "";

        notifications.innerHTML = "";

        posts.forEach(post => {

            notifications.innerHTML += `

                <div class="notification-card">

                    <h3>${post.title}</h3>

                    <p>${post.body}</p>

                </div>

            `;

        });

    }

    catch (err) {

        loading.textContent = "";

        error.textContent = err.message;

        retryBtn.style.display = "inline-block";

    }

}

loadNotifications();


// ------------------------------------
// Retry Button
// ------------------------------------

retryBtn.addEventListener("click", () => {

    loadNotifications();

});


// ------------------------------------
// Axios Example
// ------------------------------------

axios.get(
    "https://jsonplaceholder.typicode.com/users"
)

.then(response => {

    console.log("Axios Users");

    console.log(response.data);

})

.catch(error => {

    console.log(error);

});


// ------------------------------------
// Axios Async/Await
// ------------------------------------

async function axiosFetchPosts() {

    try {

        const response = await axios.get(

            "https://jsonplaceholder.typicode.com/posts",

            {

                params: {

                    _limit: 5

                }

            }

        );

        console.log("Axios Posts");

        console.log(response.data);

    }

    catch (error) {

        console.log(error);

    }

}

axiosFetchPosts();


// ------------------------------------
// Axios Request Interceptor
// ------------------------------------

axios.interceptors.request.use(config => {

    console.log("API Call Started:");

    console.log(config.url);

    return config;

});