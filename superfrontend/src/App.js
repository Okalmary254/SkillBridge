import LandingPage from "./pages/LandingPage";
import AuthPage from "./pages/AuthPage";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import "./App.css";
import UploadResume from "./pages/UploadResume";
import Dashboard from "./pages/Dashboard";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/auth" element={<AuthPage />} />
        <Route path="/upload" element={<UploadResume />} />
        <Route path="/dashboard" element={<Dashboard />} />
      </Routes>
    </Router>
  );
}

export default App;