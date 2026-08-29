CERTIFICATION_DATABASE = {
    "docker": [{"name": "Docker Certified Associate", "provider": "Docker Inc."}],
    "kubernetes": [{"name": "Certified Kubernetes Application Developer (CKAD)", "provider": "CNCF"}],
    "fastapi": [{"name": "FastAPI Course Certificate", "provider": "Udemy"}],
    "langchain": [{"name": "LangChain for LLM Application Development", "provider": "DeepLearning.AI"}],
    "deep learning": [{"name": "Deep Learning Specialization", "provider": "DeepLearning.AI"}],
}
GENERAL_CERTS = [{"name": "AMD AI PC Developer Certification", "provider": "AMD University Program"}]

def recommend_certifications(missing_skills, database=CERTIFICATION_DATABASE, general=GENERAL_CERTS):
    recommended, seen = [], set()
    for skill in missing_skills:
        if skill in database:
            for cert in database[skill]:
                if cert["name"] not in seen:
                    recommended.append({**cert, "for_skill": skill})
                    seen.add(cert["name"])
    return {"skill_based_certifications": recommended, "general_recommendations": general}