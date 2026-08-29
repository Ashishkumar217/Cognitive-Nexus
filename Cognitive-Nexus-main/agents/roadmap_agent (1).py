SKILL_RESOURCES = {
    "docker": {"time_weeks": 1, "resource": "Docker official docs + Docker Mastery course"},
    "kubernetes": {"time_weeks": 2, "resource": "Kubernetes basics on KodeKloud"},
    "fastapi": {"time_weeks": 1, "resource": "FastAPI official tutorial (fastapi.tiangolo.com)"},
    "langchain": {"time_weeks": 2, "resource": "LangChain official docs + build a RAG project"},
    "rag": {"time_weeks": 2, "resource": "Build a RAG pipeline with LangChain + ChromaDB"},
    "nlp": {"time_weeks": 2, "resource": "NLP with Python — Hugging Face course"},
    "deep learning": {"time_weeks": 3, "resource": "DeepLearning.AI Specialization (Coursera)"},
    "rest api": {"time_weeks": 1, "resource": "Build REST APIs with FastAPI or Flask"},
}
DEFAULT_RESOURCE = {"time_weeks": 1, "resource": "Search official documentation + build a small project"}

def generate_roadmap(missing_skills, resources=SKILL_RESOURCES):
    roadmap = []
    current_week = 1
    for skill in missing_skills:
        info = resources.get(skill.lower(), DEFAULT_RESOURCE)
        weeks = info["time_weeks"]
        week_range = f"Week {current_week}" if weeks == 1 else f"Week {current_week}-{current_week + weeks - 1}"
        roadmap.append({"skill": skill, "duration": week_range, "resource": info["resource"]})
        current_week += weeks
    return {"roadmap": roadmap, "total_duration_weeks": current_week - 1}