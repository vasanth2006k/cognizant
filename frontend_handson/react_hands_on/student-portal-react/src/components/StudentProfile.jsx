import { useState } from "react";

function StudentProfile() {

    const [profile, setProfile] = useState({
        name:"",
        email:"",
        semester:""
    });

    function handleChange(e){

        setProfile({
            ...profile,
            [e.target.name]:e.target.value
        });

    }

    return(

        <div className="profile">

            <h2>Student Profile</h2>

            <input
            type="text"
            name="name"
            placeholder="Enter Name"
            value={profile.name}
            onChange={handleChange}
            />

            <input
            type="email"
            name="email"
            placeholder="Enter Email"
            value={profile.email}
            onChange={handleChange}
            />

            <input
            type="text"
            name="semester"
            placeholder="Semester"
            value={profile.semester}
            onChange={handleChange}
            />

            <h3>Preview</h3>

            <p>Name : {profile.name}</p>
            <p>Email : {profile.email}</p>
            <p>Semester : {profile.semester}</p>

        </div>

    )

}

export default StudentProfile;