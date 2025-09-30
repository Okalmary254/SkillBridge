from flask import Blueprint, request, jsonify

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/upload', methods=['POST'])
def upload_resume():
    # Logic to handle resume upload
    return jsonify({"message": "Resume uploaded successfully."}), 201

@profile_bp.route('/skills', methods=['POST'])
def add_skills():
    # Logic to add manual skills
    skills = request.json.get('skills', [])
    return jsonify({"message": "Skills added successfully.", "skills": skills}), 201

# Register the blueprint in the main app file (e.g., __init__.py)
# from .routes.profile import profile_bp
# app.register_blueprint(profile_bp, url_prefix='/api/profile')