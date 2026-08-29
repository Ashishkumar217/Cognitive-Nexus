def calculate_ats_score(text, technical_skills):
    import re
    score = 0
    feedback = []

    has_email = bool(re.search(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text))
    has_phone = bool(re.search(r'\d{10}', text))
    if has_email:
        score += 10
    else:
        feedback.append("Add a professional email address")
    if has_phone:
        score += 10
    else:
        feedback.append("Add a phone number")

    skill_count = len(technical_skills)
    if skill_count >= 8:
        score += 30
    elif skill_count >= 5:
        score += 20
        feedback.append("Add more relevant technical skills")
    elif skill_count >= 1:
        score += 10
        feedback.append("Your skills section is too thin, add more")
    else:
        feedback.append("No technical skills found")

    section_keywords = ["experience", "education", "project", "skill", "certification", "achievement"]
    text_lower = text.lower()
    found_sections = [kw for kw in section_keywords if kw in text_lower]
    score += min(len(found_sections) * 5, 30)
    if len(found_sections) < 4:
        missing = [kw for kw in section_keywords if kw not in found_sections]
        feedback.append(f"Consider adding sections like: {', '.join(missing)}")

    word_count = len(text.split())
    if word_count >= 150:
        score += 20
    elif word_count >= 80:
        score += 10
        feedback.append("Resume content seems short")
    else:
        feedback.append("Resume is too short")

    score = min(score, 100)
    if not feedback:
        feedback.append("Great! Your resume covers the key ATS-friendly elements")

    return {"ats_score": score, "feedback": feedback}


def calculate_readiness_score(resume_score, dsa_score=0, projects_score=0,
                                communication_score=0, interview_score=0, consistency_score=0):
    weights = {"resume": 0.20, "dsa": 0.20, "projects": 0.20,
               "communication": 0.15, "interview": 0.15, "consistency": 0.10}

    total = (
        resume_score * weights["resume"] + dsa_score * weights["dsa"] +
        projects_score * weights["projects"] + communication_score * weights["communication"] +
        interview_score * weights["interview"] + consistency_score * weights["consistency"]
    )

    breakdown = {
        "resume": round(resume_score, 2), "dsa": round(dsa_score, 2),
        "projects": round(projects_score, 2), "communication": round(communication_score, 2),
        "interview": round(interview_score, 2), "consistency": round(consistency_score, 2)
    }
    weak_areas = [k for k, v in breakdown.items() if v < 50]

    return {"career_readiness_score": round(total, 2), "breakdown": breakdown, "weak_areas": weak_areas}