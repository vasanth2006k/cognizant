export const getAllCourses = async () => {
  return [
    {
      id: 1,
      title: "Web Development",
      body: "HTML, CSS, JavaScript, Vue.js and responsive web design."
    },
    {
      id: 2,
      title: "Python Programming",
      body: "Python fundamentals, automation, APIs and backend development."
    },
    {
      id: 3,
      title: "Data Structures",
      body: "Arrays, Linked Lists, Trees, Graphs and Algorithms."
    },
    {
      id: 4,
      title: "Machine Learning",
      body: "Build intelligent systems using Python and TensorFlow."
    },
    {
      id: 5,
      title: "Cloud Computing",
      body: "AWS, Azure, Docker and Kubernetes essentials."
    },
    {
      id: 6,
      title: "Cyber Security",
      body: "Network Security, Cryptography and Ethical Hacking."
    },
    {
      id: 7,
      title: "Java Full Stack",
      body: "Java, Spring Boot, REST APIs and MySQL."
    },
    {
      id: 8,
      title: "Mobile App Development",
      body: "Flutter development for Android and iOS."
    },
    {
      id: 9,
      title: "Artificial Intelligence",
      body: "Neural Networks, Deep Learning and Generative AI."
    }
  ];
};

export const getCourseById = async (id) => {
  const courses = await getAllCourses();
  return courses.find(course => course.id === id);
};

export const enrollStudent = async (courseId) => {
  return {
    success: true,
    message: `Successfully enrolled in course ${courseId}`
  };
};