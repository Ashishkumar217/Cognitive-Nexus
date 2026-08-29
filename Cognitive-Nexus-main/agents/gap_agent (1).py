JOB_ROLE_SKILLS = {
    "AI Engineer": ["python", "machine learning", "deep learning", "tensorflow", "pytorch",
                    "langchain", "docker", "kubernetes", "fastapi", "sql", "rest api",
                    "data science", "nlp", "rag"],
    "Data Scientist": ["python", "sql", "pandas", "numpy", "machine learning",
                       "data science", "tensorflow", "statistics", "data visualization"],
    "Full Stack Developer": ["javascript", "html", "css", "react", "node.js", "sql",
                             "git", "rest api", "python", "mongodb"],
    "Backend Developer": ["python", "java", "sql", "fastapi", "django", "flask",
                          "docker", "git", "rest api", "mongodb", "postgresql"]
}

def analyze_skill_gap(your_skills, target_role):
    if target_role not in JOB_ROLE_SKILLS:
        return {"error": f"Role '{target_role}' not found"}

    required = set(s.lower() for s in JOB_ROLE_SKILLS[target_role])
    yours = set(s.lower() for s in your_skills)
    matched = yours & required
    missing = required - yours
    match_pct = round((len(matched) / len(required)) * 100, 1) if required else 0

    return {
        "target_role": target_role,
        "matched_skills": sorted(matched),
        "missing_skills": sorted(missing),
        "match_percentage": match_pct
    }