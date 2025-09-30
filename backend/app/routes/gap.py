from flask import Blueprint, request, jsonify
from app.services.nlp import extract_skills
from app.utils import compare_skills

gap_bp = Blueprint('gap', __name__)

@gap_bp.route('/api/gap/analyze', methods=['GET'])
def analyze_gap():
    user_skills = request.args.getlist('skills')
    market_skills = request.args.getlist('market_skills')

    missing_skills = compare_skills(user_skills, market_skills)

    recommendations = generate_recommendations(missing_skills)

    return jsonify({
        'user_skills': user_skills,
        'market_skills': market_skills,
        'missing_skills': missing_skills,
        'recommendations': recommendations
    })

def generate_recommendations(missing_skills):
    # Placeholder for actual recommendation logic
    return [{"skill": skill, "resource": f"{skill} Learning Resource"} for skill in missing_skills]