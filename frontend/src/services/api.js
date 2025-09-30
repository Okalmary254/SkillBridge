import axios from 'axios';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
});

// Function to upload a resume
export const uploadResume = (formData) => {
  return api.post('/profile/upload', formData);
};

// Function to add manual skills
export const addSkills = (skills) => {
  return api.post('/profile/skills', { skills });
};

// Function to analyze skill gaps
export const analyzeGap = () => {
  return api.get('/gap/analyze');
};

// Function to get learning recommendations
export const getRecommendations = () => {
  return api.get('/recommendations');
};