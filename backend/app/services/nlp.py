
import spacy
from typing import List, Dict, Any

# Load the spaCy model for NLP tasks
nlp = spacy.load("en_core_web_sm")

def extract_skills(text: str, skill_keywords: List[str] = None) -> List[str]:
    """
    Extract skills from the provided text using NLP and keyword matching.
    Args:
        text (str): The text from which to extract skills.
        skill_keywords (List[str], optional): List of known skills to match. If None, uses a default set.
    Returns:
        List[str]: A list of extracted skills.
    """
    doc = nlp(text)
    if skill_keywords is None:
        skill_keywords = [
            "Python", "Java", "JavaScript", "SQL", "Flask", "React", "HTML", "CSS", "Django", "C++", "C#", "AWS", "Docker", "Kubernetes", "TensorFlow", "Pandas", "Node.js", "Angular", "Vue", "Linux", "Git", "CI/CD", "PostgreSQL", "Redis", "Figma", "Redux", "Unit Testing", "Data Visualization", "Machine Learning"
        ]
    found_skills = set()
    # Token-based matching
    for token in doc:
        if token.text in skill_keywords:
            found_skills.add(token.text)
    # Phrase-based matching (for multi-word skills)
    text_lower = text.lower()
    for skill in skill_keywords:
        if " " in skill:
            if skill.lower() in text_lower:
                found_skills.add(skill)
    return list(found_skills)

def extract_entities(text: str) -> List[Dict[str, Any]]:
    """
    Extract named entities (ORG, PERSON, GPE, etc.) from text.
    Args:
        text (str): The text to analyze.
    Returns:
        List[Dict[str, Any]]: List of entities with type and value.
    """
    doc = nlp(text)
    return [{"text": ent.text, "label": ent.label_} for ent in doc.ents]

def extract_keywords(text: str, top_n: int = 10) -> List[str]:
    """
    Extract top keywords from text using simple noun chunking and frequency.
    Args:
        text (str): The text to analyze.
        top_n (int): Number of keywords to return.
    Returns:
        List[str]: List of keywords.
    """
    doc = nlp(text)
    freq = {}
    for chunk in doc.noun_chunks:
        key = chunk.text.lower().strip()
        freq[key] = freq.get(key, 0) + 1
    sorted_keywords = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return [kw for kw, _ in sorted_keywords[:top_n]]

def clean_text(text: str) -> str:
    """
    Clean and normalize text for NLP processing.
    Args:
        text (str): Raw text.
    Returns:
        str: Cleaned text.
    """
    import re
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text