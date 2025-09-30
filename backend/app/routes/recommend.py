from flask import Blueprint, jsonify, request

recommend_bp = Blueprint('recommend', __name__)

@recommend_bp.route('/api/recommendations', methods=['GET'])
def get_recommendations():
    # Sample data for demonstration purposes
    recommendations = [
        {"skill": "Flask", "resource": "Flask Mega Tutorial"},
        {"skill": "React", "resource": "React Docs Tutorial"}
    ]
    return jsonify(recommendations)

@recommend_bp.route('/api/recommendations', methods=['POST'])
def add_recommendation():
    data = request.get_json()
    # Here you would typically add the recommendation to a database
    return jsonify({"message": "Recommendation added", "data": data}), 201