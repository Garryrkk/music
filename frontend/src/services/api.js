import axios from "axios";

const API = axios.create({
    baseURL: "http://localhost:8000/api",
    timeout: 5000,
    headers: {
        "Content-Type": "application/json",
    },
});

export const uploadImage = (formData) => API.post("/recommendations/recommend/", formData);
export const fetchUserProfile = () => API.get("/users/profile/");
