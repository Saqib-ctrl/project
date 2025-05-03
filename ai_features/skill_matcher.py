from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_skill_match(candidate_skills, job_skills):
    all_skills = [" ".join(candidate_skills), " ".join(job_skills)]
    vectorizer = TfidfVectorizer().fit_transform(all_skills)
    similarity = cosine_similarity(vectorizer[0:1], vectorizer[1:2])[0][0]
    return round(similarity * 100, 2)