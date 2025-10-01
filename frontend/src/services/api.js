import axios from 'axios';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
});

// Function to upload a resume
export const uploadResume = (formData) => {
  return api.post('/api/profile/upload', formData);
};

// Function to add manual skills
export const addSkills = (skills) => {
  return api.post('/api/profile/skills', { skills });
};

// Function to analyze skill gaps
export const analyzeGap = () => {
  return api.get('/api/gap/analyze');
};

// Function to get learning recommendations
export const getRecommendations = () => {
  return api.get('/api/recommendations');
};