import re
import difflib
from typing import List, Dict, Set, Tuple


def some_utility_function():
    # This function can be used for various utility tasks
    pass


def compare_skills(user_skills: List[str], market_skills: List[str]) -> List[str]:
    """
    Compare user skills with market demands and return missing skills.
    
    Args:
        user_skills: List of skills the user currently has
        market_skills: List of skills demanded by the market/job
    
    Returns:
        List of skills that are missing from user's skillset
    """
    # Normalize skills to lowercase for comparison
    user_skills_normalized = {skill.lower().strip() for skill in user_skills}
    market_skills_normalized = {skill.lower().strip() for skill in market_skills}
    
    # Find missing skills
    missing_skills = market_skills_normalized - user_skills_normalized
    
    # Return original case market skills that are missing
    missing_original = []
    for market_skill in market_skills:
        if market_skill.lower().strip() in missing_skills:
            missing_original.append(market_skill)
    
    return missing_original


def normalize_skill_name(skill: str) -> str:
    """
    Normalize skill names for better matching.
    
    Args:
        skill: Raw skill name
    
    Returns:
        Normalized skill name
    """
    # Remove special characters and normalize whitespace
    normalized = re.sub(r'[^\w\s+#.]', '', skill)
    normalized = re.sub(r'\s+', ' ', normalized).strip()
    return normalized.lower()


def calculate_skill_similarity(skill1: str, skill2: str) -> float:
    """
    Calculate similarity between two skills using fuzzy matching.
    
    Args:
        skill1: First skill to compare
        skill2: Second skill to compare
    
    Returns:
        Similarity score between 0 and 1
    """
    normalized1 = normalize_skill_name(skill1)
    normalized2 = normalize_skill_name(skill2)
    
    return difflib.SequenceMatcher(None, normalized1, normalized2).ratio()


def find_similar_skills(target_skill: str, skill_list: List[str], threshold: float = 0.7) -> List[Tuple[str, float]]:
    """
    Find skills similar to the target skill.
    
    Args:
        target_skill: The skill to find matches for
        skill_list: List of skills to search in
        threshold: Minimum similarity threshold (0-1)
    
    Returns:
        List of tuples (skill, similarity_score) sorted by similarity
    """
    similarities = []
    
    for skill in skill_list:
        similarity = calculate_skill_similarity(target_skill, skill)
        if similarity >= threshold:
            similarities.append((skill, similarity))
    
    # Sort by similarity score (descending)
    similarities.sort(key=lambda x: x[1], reverse=True)
    
    return similarities


def extract_skills_from_text(text: str, skill_keywords: List[str]) -> List[str]:
    """
    Extract skills from text based on keyword matching.
    
    Args:
        text: Text to extract skills from
        skill_keywords: List of known skill keywords
    
    Returns:
        List of found skills
    """
    found_skills = []
    text_lower = text.lower()
    
    for skill in skill_keywords:
        skill_lower = skill.lower()
        # Use word boundaries to avoid partial matches
        pattern = r'\b' + re.escape(skill_lower) + r'\b'
        if re.search(pattern, text_lower):
            found_skills.append(skill)
    
    return found_skills


def categorize_skills(skills: List[str]) -> Dict[str, List[str]]:
    """
    Categorize skills into different types.
    
    Args:
        skills: List of skills to categorize
    
    Returns:
        Dictionary with skill categories as keys and skill lists as values
    """
    # Predefined skill categories with common keywords
    categories = {
        'Programming Languages': ['python', 'java', 'javascript', 'c++', 'c#', 'php', 'ruby', 'go', 'rust', 'scala'],
        'Web Technologies': ['html', 'css', 'react', 'angular', 'vue', 'nodejs', 'express', 'django', 'flask'],
        'Databases': ['sql', 'mysql', 'postgresql', 'mongodb', 'redis', 'sqlite', 'oracle'],
        'Cloud Platforms': ['aws', 'azure', 'gcp', 'docker', 'kubernetes', 'terraform'],
        'Data Science': ['pandas', 'numpy', 'sklearn', 'tensorflow', 'pytorch', 'tableau', 'power bi'],
        'Tools & DevOps': ['git', 'jenkins', 'ci/cd', 'linux', 'bash', 'vim', 'jira'],
        'Soft Skills': ['communication', 'leadership', 'teamwork', 'problem solving', 'project management']
    }
    
    categorized = {category: [] for category in categories.keys()}
    categorized['Other'] = []
    
    for skill in skills:
        skill_lower = skill.lower()
        categorized_flag = False
        
        for category, keywords in categories.items():
            if any(keyword in skill_lower for keyword in keywords):
                categorized[category].append(skill)
                categorized_flag = True
                break
        
        if not categorized_flag:
            categorized['Other'].append(skill)
    
    # Remove empty categories
    return {k: v for k, v in categorized.items() if v}


# Additional utility functions can be added here as needed.