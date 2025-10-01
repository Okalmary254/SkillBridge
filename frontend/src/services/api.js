import axios from 'axios';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
});


// ------------------- PROFILE & AUTH -------------------

// Register a new user (Signup)
export const registerUser = (userData) => {
  // POST /api/profile/profile (custom, for demo)
  return api.post('/api/profile/profile', userData);
};

// Login user (simulate, for demo)
export const loginUser = (credentials) => {
  // POST /api/profile/login (not implemented in backend, placeholder)
  return api.post('/api/profile/login', credentials);
};

// Get user profile
export const getProfile = () => {
  // GET /api/profile/profile
  return api.get('/api/profile/profile');
};

// Update user profile
export const updateProfile = (profileData) => {
  // PUT /api/profile/profile
  return api.put('/api/profile/profile', profileData);
};

// Delete user profile
export const deleteProfile = () => {
  // DELETE /api/profile/profile
  return api.delete('/api/profile/profile');
};

// Upload resume file
export const uploadResume = (formData) => {
  // POST /api/profile/upload
  return api.post('/api/profile/upload', formData);
};

// Add manual skills
export const addSkills = (skills) => {
  // POST /api/profile/skills
  return api.post('/api/profile/skills', { skills });
};

// ------------------- JOB DATA -------------------

// Get job market data
export const getJobData = () => {
  // GET /api/jobdata
  return api.get('/api/jobdata');
};

// ------------------- GAP ANALYSIS -------------------

// Analyze skill gap (POST recommended for detailed input)
export const analyzeGap = (data) => {
  // POST /api/gap/analyze
  return api.post('/api/gap/analyze', data);
};

// ------------------- RECOMMENDATIONS -------------------

// Get learning recommendations (POST for detailed, GET for default)
export const getRecommendations = (data) => {
  // POST /api/recommendations (detailed), GET /api/recommendations (default)
  if (data) {
    return api.post('/api/recommendations', data);
  }
  return api.get('/api/recommendations');
};

// Add a manual recommendation (admin/testing)
export const addManualRecommendation = (rec) => {
  // POST /api/recommendations/manual
  return api.post('/api/recommendations/manual', rec);
};