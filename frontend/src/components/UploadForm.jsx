import React, { useState } from 'react';

const UploadForm = () => {
    const [file, setFile] = useState(null);
    const [skills, setSkills] = useState('');

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handleSkillsChange = (e) => {
        setSkills(e.target.value);
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        // Handle file upload and skills submission
        // API calls to backend will be implemented here
    };

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label htmlFor="resume-upload">Upload Resume:</label>
                <input
                    type="file"
                    id="resume-upload"
                    accept=".pdf, .doc, .docx"
                    onChange={handleFileChange}
                />
            </div>
            <div>
                <label htmlFor="manual-skills">Or Enter Skills Manually:</label>
                <textarea
                    id="manual-skills"
                    value={skills}
                    onChange={handleSkillsChange}
                    placeholder="Enter your skills separated by commas"
                />
            </div>
            <button type="submit">Submit</button>
        </form>
    );
};

export default UploadForm;