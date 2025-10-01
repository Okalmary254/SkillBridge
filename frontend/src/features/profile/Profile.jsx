import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import Loader from '../../components/Loader';

const Profile = () => {
  const [profile, setProfile] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [editMode, setEditMode] = useState(false);
  const [form, setForm] = useState({});
  const navigate = useNavigate();

  useEffect(() => {
    const fetchProfile = async () => {
      setLoading(true);
      setError('');
      try {
        const res = await axios.get('/api/profile/profile');
        setProfile(res.data);
        setForm(res.data);
      } catch (err) {
        setError('Failed to load profile.');
      } finally {
        setLoading(false);
      }
    };
    fetchProfile();
  }, []);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleEdit = () => setEditMode(true);
  const handleCancel = () => {
    setEditMode(false);
    setForm(profile);
  };

  const handleSave = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    try {
      const res = await axios.put('/api/profile/profile', form);
      setProfile(res.data.profile);
      setEditMode(false);
    } catch (err) {
      setError('Failed to update profile.');
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async () => {
    if (!window.confirm('Are you sure you want to delete your profile?')) return;
    setLoading(true);
    setError('');
    try {
      await axios.delete('/api/profile/profile');
      localStorage.removeItem('user');
      navigate('/signup');
    } catch (err) {
      setError('Failed to delete profile.');
    } finally {
      setLoading(false);
    }
  };

  if (loading) return <Loader text="Loading profile..." />;
  if (error) return <div className="text-red-600 text-center mt-8">{error}</div>;
  if (!profile) return null;

  return (
    <div className="max-w-2xl mx-auto mt-10 bg-white rounded shadow p-8">
      <h2 className="text-2xl font-bold mb-4">My Profile</h2>
      {editMode ? (
        <form onSubmit={handleSave} className="space-y-4">
          <div>
            <label className="block mb-1 font-medium">Name</label>
            <input
              type="text"
              name="name"
              value={form.name || ''}
              onChange={handleChange}
              className="w-full border px-3 py-2 rounded"
              required
            />
          </div>
          <div>
            <label className="block mb-1 font-medium">Email</label>
            <input
              type="email"
              name="email"
              value={form.email || ''}
              onChange={handleChange}
              className="w-full border px-3 py-2 rounded"
              required
            />
          </div>
          <div>
            <label className="block mb-1 font-medium">Location</label>
            <input
              type="text"
              name="location"
              value={form.location || ''}
              onChange={handleChange}
              className="w-full border px-3 py-2 rounded"
            />
          </div>
          <div>
            <label className="block mb-1 font-medium">Bio</label>
            <textarea
              name="bio"
              value={form.bio || ''}
              onChange={handleChange}
              className="w-full border px-3 py-2 rounded"
              rows={3}
            />
          </div>
          <div className="flex gap-4">
            <button
              type="submit"
              className="bg-blue-600 text-white px-4 py-2 rounded font-semibold hover:bg-blue-700 transition"
              disabled={loading}
            >
              Save
            </button>
            <button
              type="button"
              onClick={handleCancel}
              className="bg-gray-300 text-gray-800 px-4 py-2 rounded font-semibold hover:bg-gray-400 transition"
            >
              Cancel
            </button>
          </div>
        </form>
      ) : (
        <div className="space-y-3">
          <div>
            <span className="font-medium">Name:</span> {profile.name}
          </div>
          <div>
            <span className="font-medium">Email:</span> {profile.email}
          </div>
          <div>
            <span className="font-medium">Location:</span> {profile.location}
          </div>
          <div>
            <span className="font-medium">Bio:</span> {profile.bio}
          </div>
          <div>
            <span className="font-medium">Skills:</span> {profile.skills?.join(', ') || 'N/A'}
          </div>
          <div>
            <span className="font-medium">Education:</span>
            <ul className="list-disc ml-6">
              {profile.education?.map((edu, idx) => (
                <li key={idx}>
                  {edu.degree} - {edu.institution} ({edu.year})
                </li>
              )) || <li>N/A</li>}
            </ul>
          </div>
          <div>
            <span className="font-medium">Experience:</span>
            <ul className="list-disc ml-6">
              {profile.experience?.map((exp, idx) => (
                <li key={idx}>
                  {exp.title} at {exp.company} ({exp.years})
                </li>
              )) || <li>N/A</li>}
            </ul>
          </div>
          {profile.resume_url && (
            <div>
              <span className="font-medium">Resume:</span>{' '}
              <a
                href={profile.resume_url}
                target="_blank"
                rel="noopener noreferrer"
                className="text-blue-600 hover:underline"
              >
                View Resume
              </a>
            </div>
          )}
          <div className="flex gap-4 mt-4">
            <button
              onClick={handleEdit}
              className="bg-blue-600 text-white px-4 py-2 rounded font-semibold hover:bg-blue-700 transition"
            >
              Edit Profile
            </button>
            <button
              onClick={handleDelete}
              className="bg-red-600 text-white px-4 py-2 rounded font-semibold hover:bg-red-700 transition"
            >
              Delete Profile
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default Profile;
