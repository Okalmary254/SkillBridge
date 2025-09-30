
from flask import Blueprint, request, jsonify
import uuid

profile_bp = Blueprint('profile', __name__)

# In-memory mock user profile store (for demonstration)
mock_user_profile = {
    "user_id": str(uuid.uuid4()),
    "name": "Jane Doe",
    "email": "jane.doe@email.com",
    "location": "Nairobi, Kenya",
    "bio": "Software engineer passionate about building impactful products.",
    "skills": ["Python", "Flask", "React"],
    "education": [
        {"degree": "BSc Computer Science", "institution": "University of Nairobi", "year": 2021}
    ],
    "experience": [
        {"title": "Software Engineer", "company": "TechNova", "years": "2021-2023"}
    ],
    "resume_url": None
}


@profile_bp.route('/upload', methods=['POST'])
def upload_resume():
    # Simulate resume upload and update profile
    file = request.files.get('resume')
    if file:
        # In a real app, save file and generate URL
        mock_user_profile['resume_url'] = f"/static/resumes/{mock_user_profile['user_id']}.pdf"
        return jsonify({"message": "Resume uploaded successfully.", "resume_url": mock_user_profile['resume_url']}), 201
    return jsonify({"error": "No resume file provided."}), 400


@profile_bp.route('/skills', methods=['POST'])
def add_skills():
    # Add manual skills to user profile
    skills = request.json.get('skills', [])
    if not isinstance(skills, list):
        return jsonify({"error": "Skills must be a list."}), 400
    mock_user_profile['skills'].extend([s for s in skills if s not in mock_user_profile['skills']])
    return jsonify({"message": "Skills added successfully.", "skills": mock_user_profile['skills']}), 201


# Get user profile
@profile_bp.route('/profile', methods=['GET'])
def get_profile():
    return jsonify(mock_user_profile)

# Update user profile
@profile_bp.route('/profile', methods=['PUT'])
def update_profile():
    data = request.get_json()
    for field in ["name", "email", "location", "bio"]:
        if field in data:
            mock_user_profile[field] = data[field]
    # Optionally update education and experience
    if "education" in data and isinstance(data["education"], list):
        mock_user_profile["education"] = data["education"]
    if "experience" in data and isinstance(data["experience"], list):
        mock_user_profile["experience"] = data["experience"]
    return jsonify({"message": "Profile updated successfully.", "profile": mock_user_profile})

# Delete user profile (mock)
@profile_bp.route('/profile', methods=['DELETE'])
def delete_profile():
    global mock_user_profile
    mock_user_profile = None
    return jsonify({"message": "Profile deleted."})

# Register the blueprint in the main app file (e.g., __init__.py)
# from .routes.profile import profile_bp
# app.register_blueprint(profile_bp, url_prefix='/api/profile')