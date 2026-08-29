INTENT_CATEGORIES = {
    "readiness": "career readiness score, overall progress, weak areas",
    "ats": "resume ATS score, resume quality",
    "skills": "what skills the candidate has",
    "skill_gap": "missing skills, skill gap for a target role",
    "roadmap": "learning plan, what to learn next, timeline",
    "projects": "project ideas, what projects to build",
    "certifications": "certifications to pursue",
    "resume_improvement": "how to improve the resume, resume feedback",
    "interview": "interview preparation, interview questions",
    "jobs": "job openings, job matches, applying to jobs",
    "general": "general greeting or unclear intent",
}

def classify_intent(user_message, call_llm_fn):
    categories_desc = "\n".join([f"- {k}: {v}" for k, v in INTENT_CATEGORIES.items()])
    prompt = f"""Classify this question into exactly ONE category. Respond with ONLY the category name.

Categories:
{categories_desc}

Question: "{user_message}"
Category:"""
    result = call_llm_fn(prompt, temperature=0.1, max_tokens=20).strip().lower()
    for category in INTENT_CATEGORIES:
        if category in result:
            return category
    return "general"