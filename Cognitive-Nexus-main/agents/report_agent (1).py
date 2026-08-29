from datetime import datetime

def generate_final_report(skills_data, readiness_data, gap_data, roadmap_data,
                           projects_data, certs_data, improvements_data, interview_data):
    return {
        "generated_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "career_readiness": readiness_data.get("readiness", {}),
        "ats_analysis": readiness_data.get("ats", {}),
        "skill_gap_analysis": gap_data,
        "learning_roadmap": roadmap_data,
        "recommended_projects": projects_data,
        "recommended_certifications": certs_data,
        "resume_improvement_suggestions": improvements_data,
        "interview_preparation": interview_data
    }