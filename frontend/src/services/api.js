import axios from "axios";

const API = axios.create({
    baseURL: "http://localhost:8000"
});

export const getKeywords = () => API.get("/keywords");
export const addKeyword = (name) => API.post("/keywords", { name });
export const deleteKeyword = (id) => API.delete(`/keywords/${id}`);
