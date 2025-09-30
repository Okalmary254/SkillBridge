from flask import jsonify
import spacy

# Load the spaCy model for NLP tasks
nlp = spacy.load("en_core_web_sm")

def extract_skills(text):
    """
    Extract skills from the provided text using NLP.
    
    Args:
        text (str): The text from which to extract skills.
        
    Returns:
        list: A list of extracted skills.
    """
    doc = nlp(text)
    skills = set()

    # Define a simple list of skills for demonstration purposes
    predefined_skills = {"Python", "Java", "JavaScript", "SQL", "Flask", "React", "HTML", "CSS"}

    for token in doc:
        if token.text in predefined_skills:
            skills.add(token.text)

    return list(skills)