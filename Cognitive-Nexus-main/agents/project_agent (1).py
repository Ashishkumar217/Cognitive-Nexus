PROJECT_DATABASE = {
    "AI Engineer": {
        "beginner": [
            {"name": "Resume ATS Analyzer", "skills": ["python", "nlp"], "description": "Build a tool that scores resumes against job descriptions"},
        ],
        "intermediate": [
            {"name": "RAG-based Document Q&A", "skills": ["langchain", "rag", "python"], "description": "Answer questions from PDF documents"},
        ],
        "advanced": [
            {"name": "Multi-Agent Career Assistant", "skills": ["langchain", "docker", "kubernetes"], "description": "Build a multi-agent system"},
        ]
    }
}

def recommend_projects(target_role, existing_skills, missing_skills, database=PROJECT_DATABASE):
    if target_role not in database:
        return {"error": f"No projects found for role: {target_role}"}
    recommendations = {"beginner": [], "intermediate": [], "advanced": []}
    for level in ["beginner", "intermediate", "advanced"]:
        for project in database[target_role][level]:
            project_skills = set(project["skills"])
            overlap = project_skills & set(existing_skills)
            needed = project_skills & set(missing_skills)
            recommendations[level].append({
                "name": project["name"], "description": project["description"],
                "uses_existing_skills": sorted(overlap), "builds_new_skills": sorted(needed)
            })
    return recommendations