import React, { useState } from "react";

const initialState = {
    firstName: "",
    lastName: "",
    email: "",
    phone: "",
    bio: "",
    location: "",
    website: "",
    linkedin: "",
    github: "",
    twitter: "",
    avatar: null,
};

export default function EditProfile({ profile = {}, onSave }) {
    const [form, setForm] = useState({ ...initialState, ...profile });
    const [avatarPreview, setAvatarPreview] = useState(profile.avatar || null);

    const handleChange = (e) => {
        const { name, value, files } = e.target;
        if (name === "avatar" && files[0]) {
            setForm((f) => ({ ...f, avatar: files[0] }));
            setAvatarPreview(URL.createObjectURL(files[0]));
        } else {
            setForm((f) => ({ ...f, [name]: value }));
        }
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        if (onSave) onSave(form);
    };

    return (
        <form className="edit-profile-form" onSubmit={handleSubmit} style={{ maxWidth: 500, margin: "0 auto" }}>
            <h2>Edit Profile</h2>
            <div>
                <label>Avatar</label><br />
                {avatarPreview && (
                    <img src={avatarPreview} alt="Avatar Preview" style={{ width: 80, height: 80, borderRadius: "50%", objectFit: "cover" }} />
                )}
                <input type="file" name="avatar" accept="image/*" onChange={handleChange} />
            </div>
            <div>
                <label>First Name</label>
                <input name="firstName" value={form.firstName} onChange={handleChange} required />
            </div>
            <div>
                <label>Last Name</label>
                <input name="lastName" value={form.lastName} onChange={handleChange} required />
            </div>
            <div>
                <label>Email</label>
                <input name="email" type="email" value={form.email} onChange={handleChange} required />
            </div>
            <div>
                <label>Phone</label>
                <input name="phone" type="tel" value={form.phone} onChange={handleChange} />
            </div>
            <div>
                <label>Location</label>
                <input name="location" value={form.location} onChange={handleChange} />
            </div>
            <div>
                <label>Bio</label>
                <textarea name="bio" value={form.bio} onChange={handleChange} rows={3} />
            </div>
            <div>
                <label>Website</label>
                <input name="website" type="url" value={form.website} onChange={handleChange} />
            </div>
            <div>
                <label>LinkedIn</label>
                <input name="linkedin" type="url" value={form.linkedin} onChange={handleChange} />
            </div>
            <div>
                <label>GitHub</label>
                <input name="github" type="url" value={form.github} onChange={handleChange} />
            </div>
            <div>
                <label>Twitter</label>
                <input name="twitter" type="url" value={form.twitter} onChange={handleChange} />
            </div>
            <button type="submit" style={{ marginTop: 16 }}>Save Changes</button>
        </form>
    );
}