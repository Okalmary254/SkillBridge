
from flask import Blueprint, request, jsonify
import json
import jwt
from flask import current_app
from app.models import db, User, Skill

profile_bp = Blueprint('profile', __name__)

def get_user_from_token():
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return None
    token = auth_header.split(' ')[1]
    try:
        payload = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
        user = User.query.get(payload['user_id'])
        return user
    except Exception:
        return None


@profile_bp.route('/upload', methods=['POST'])
def upload_resume():
    user = get_user_from_token()
    if not user:
        return jsonify({'error': 'Unauthorized'}), 401
    file = request.files.get('resume')
    if file:
        # In a real app, save file and generate URL
        filename = f"user_{user.id}_resume.pdf"
        file.save(f"static/resumes/{filename}")
        user.resume_url = f"/static/resumes/{filename}"
        db.session.commit()
        return jsonify({"message": "Resume uploaded successfully.", "resume_url": user.resume_url}), 201
    return jsonify({"error": "No resume file provided."}), 400



# Add skills (append new skills)
@profile_bp.route('/skills', methods=['POST'])
def add_skills():
    user = get_user_from_token()
    if not user:
        return jsonify({'error': 'Unauthorized'}), 401
    skills = request.json.get('skills', [])
    if not isinstance(skills, list):
        return jsonify({"error": "Skills must be a list."}), 400
    existing = {s.name for s in user.skills}
    for skill in skills:
        if skill not in existing:
            db.session.add(Skill(name=skill, user_id=user.id))
    db.session.commit()
    return jsonify({"message": "Skills added successfully.", "skills": [s.name for s in user.skills]}), 201

# Remove a skill by name
@profile_bp.route('/skills', methods=['DELETE'])
def remove_skill():
    user = get_user_from_token()
    if not user:
        return jsonify({'error': 'Unauthorized'}), 401
    skill_name = request.json.get('skill')
    if not skill_name:
        return jsonify({'error': 'Skill name required.'}), 400
    skill = Skill.query.filter_by(user_id=user.id, name=skill_name).first()
    if not skill:
        return jsonify({'error': 'Skill not found.'}), 404
    db.session.delete(skill)
    db.session.commit()
    return jsonify({'message': 'Skill removed.', 'skills': [s.name for s in user.skills]}), 200

# Replace all skills (set skills)
@profile_bp.route('/skills', methods=['PUT'])
def set_skills():
    user = get_user_from_token()
    if not user:
        return jsonify({'error': 'Unauthorized'}), 401
    skills = request.json.get('skills', [])
    if not isinstance(skills, list):
        return jsonify({"error": "Skills must be a list."}), 400
    # Remove all current skills
    Skill.query.filter_by(user_id=user.id).delete()
    # Add new skills
    for skill in skills:
        db.session.add(Skill(name=skill, user_id=user.id))
    db.session.commit()
    return jsonify({"message": "Skills updated.", "skills": [s.name for s in user.skills]}), 200



# Get user profile
@profile_bp.route('/profile', methods=['GET'])
def get_profile():
    user = get_user_from_token()
    if not user:
        return jsonify({'error': 'Unauthorized'}), 401
    profile = {
        'id': user.id,
        'name': user.username,
        'email': user.email,
        'location': user.location,
        'bio': user.bio,
        'skills': [s.name for s in user.skills],
        'education': json.loads(user.education) if user.education else [],
        'experience': json.loads(user.experience) if user.experience else [],
        'resume_url': user.resume_url,
        'image_url': user.image_url
    }
    return jsonify(profile)

# Update user profile
@profile_bp.route('/profile', methods=['PUT'])
def update_profile():
    user = get_user_from_token()
    if not user:
        return jsonify({'error': 'Unauthorized'}), 401
    data = request.get_json()
    # Only allow updating certain fields
    if 'name' in data:
        user.username = data['name']
    if 'email' in data:
        user.email = data['email']
    if 'location' in data:
        user.location = data['location']
    if 'bio' in data:
        user.bio = data['bio']
    if 'education' in data:
        user.education = json.dumps(data['education'])
    if 'experience' in data:
        user.experience = json.dumps(data['experience'])
    if 'image_url' in data:
        user.image_url = data['image_url']
    db.session.commit()
    profile = {
        'id': user.id,
        'name': user.username,
        'email': user.email,
        'location': user.location,
        'bio': user.bio,
        'skills': [s.name for s in user.skills],
        'education': json.loads(user.education) if user.education else [],
        'experience': json.loads(user.experience) if user.experience else [],
        'resume_url': user.resume_url,
        'image_url': user.image_url
    }
    return jsonify({'message': 'Profile updated successfully.', 'profile': profile})

# Delete user profile (mock)
@profile_bp.route('/profile', methods=['DELETE'])
def delete_profile():
    user = get_user_from_token()
    if not user:
        return jsonify({'error': 'Unauthorized'}), 401
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "Profile deleted."})

# Register the blueprint in the main app file (e.g., __init__.py)
# from .routes.profile import profile_bp
# app.register_blueprint(profile_bp, url_prefix='/api/profile')