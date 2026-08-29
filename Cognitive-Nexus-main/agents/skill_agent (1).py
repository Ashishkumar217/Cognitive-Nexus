import re
import json

TECHNICAL_SKILLS = [
    "Python", "Java", "JavaScript", "C++", "C", "SQL", "HTML", "CSS",
    "React", "Node.js", "FastAPI", "Django", "Flask", "MongoDB",
    "PostgreSQL", "MySQL", "AWS", "Azure", "Docker", "Kubernetes",
    "Git", "GitHub", "TypeScript", "Machine Learning", "Deep Learning",
    "AI", "Artificial Intelligence", "Data Science", "TensorFlow",
    "PyTorch", "NumPy", "Pandas", "LangChain", "REST API", "Linux",
    "DSA", "Data Structures", "Algorithms", "OOP", "DBMS"
]

SOFT_SKILLS = [
    "Leadership", "Communication", "Teamwork", "Problem Solving",
    "Collaboration", "Analytics", "Innovation", "Digital Marketing",
    "Time Management", "Critical Thinking", "Adaptability"
]

def extract_skills_regex(text):
    text_lower = text.lower()
    technical = [s for s in TECHNICAL_SKILLS if s.lower() in text_lower]
    soft = [s for s in SOFT_SKILLS if s.lower() in text_lower]
    return {"technical": technical, "soft": soft}

def extract_education(text):
    entries = []
    degree_keywords = ["bachelor of", "b.sc.", "diploma in", "senior secondary education"]
    for line in text.split("\n"):
        line_stripped = line.strip()
        if any(kw in line_stripped.lower() for kw in degree_keywords) and len(line_stripped) < 60:
            entries.append(line_stripped)
    return entries

def extract_projects(text):
    text_upper = text.upper()
    if "PROJECTS" not in text_upper:
        return []
    start = text_upper.find("PROJECTS") + len("PROJECTS")
    end = text_upper.find("\nSKILLS", start)
    if end == -1:
        end = len(text)
    section = text[start:end].strip()
    return [l.strip() for l in section.split("\n") if l.strip()]

def llm_extract_resume_data(resume_text, call_llm_fn):
    prompt = f"""Extract structured information from this resume. Return ONLY valid JSON, no other text.

Format:
{{
  "technical_skills": ["skill1", "skill2"],
  "soft_skills": ["skill1", "skill2"],
  "education": ["degree - institution - year"],
  "projects": [{{"name": "project name", "description": "one sentence summary"}}],
  "years_of_relevant_experience_estimate": "e.g. '0-1 years'"
}}

RESUME:
{resume_text[:2000]}

Return ONLY the JSON object."""
    raw = call_llm_fn(prompt, temperature=0.2, max_tokens=500)
    try:
        return json.loads(raw)
    except Exception:
        match = re.search(r'\{.*\}', raw, re.DOTALL)
        if match:
            try:
                return json.loads(match.group(0))
            except Exception:
                return {}
        return {}