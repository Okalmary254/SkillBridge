import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

import "./App.css";

import LandingPage from "./pages/LandingPage";
import AuthPage from "./pages/AuthPage";
import UploadResume from "./pages/UploadResume";
import Dashboard from "./pages/Dashboard";
import Roadmap from "./pages/Roadmap";

function App() {
  return (
    <Router>
      <Routes>
        {/* Landing Page */}
        <Route path="/" element={<LandingPage />} />

        {/* Authentication */}
        <Route path="/auth" element={<AuthPage />} />

        {/* Resume Upload */}
        <Route path="/upload" element={<UploadResume />} />

        {/* User Dashboard */}
        <Route path="/dashboard" element={<Dashboard />} />

        {/* Learning Roadmap */}
        <Route path="/roadmap" element={<Roadmap />} />
      </Routes>
    </Router>
  );
}

export default App;
