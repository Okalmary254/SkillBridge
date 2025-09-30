from flask import Blueprint, jsonify

jobdata_bp = Blueprint('jobdata', __name__)

@jobdata_bp.route('/api/jobdata', methods=['GET'])
def get_job_data():
    # Mock job data for demonstration purposes
    job_data = [
        {"title": "Software Engineer", "skills": ["Python", "Flask", "React"]},
        {"title": "Data Scientist", "skills": ["Python", "SQL", "Machine Learning"]},
        {"title": "Frontend Developer", "skills": ["JavaScript", "React", "CSS"]},
    ]
    return jsonify(job_data)