<p align="center">
  <img src="assets/banner%20%282%29.png" alt="Cognitive Nexus Banner" width="100%">
</p>

# Cognitive Nexus

### Multi-Agent Career Intelligence System

Built using **LLMs • LangChain • Ollama • AMD AI Compute**

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)

![LangChain](https://img.shields.io/badge/LangChain-AgenticAI-green)

![Ollama](https://img.shields.io/badge/Ollama-Qwen-purple)

![AMD](https://img.shields.io/badge/AMD-AI-red)


## 📖 Overview

**COGNITIVE NEXUS** is a **Multi-Agent Career Intelligence System** built using **LLMs, LangChain, Ollama (Qwen)** and **AMD AI Compute**.

The system acts as an autonomous AI career mentor by orchestrating multiple specialized AI agents that work together to analyze resumes, identify technical and soft skills, calculate career readiness, detect skill gaps, recommend personalized learning roadmaps, suggest projects and certifications, prepare interview questions, match job roles, and generate a comprehensive career report.

Unlike traditional resume analyzers, Cognitive Nexus follows an **Agentic AI architecture**, where each agent is responsible for a dedicated task while collaborating with other agents to deliver intelligent, structured, and personalized end-to-end career guidance.


# ✨ Key Features

- 📄 Intelligent Resume Parsing
- 🧠 AI-powered Skill Extraction
- 📊 Career Readiness Score
- 🔍 Skill Gap Detection
- 🗺️ Personalized Learning Roadmap
- 💡 AI Project Recommendation
- 🎓 Certification Recommendation
- 📝 Resume Improvement Suggestions
- 🎤 Interview Preparation Agent
- 💼 Job Matching Agent
- 📈 Interactive Visualizations
- 📑 Professional PDF Report Generation
- 🤖 Multi-Agent AI Pipeline
- 💬 AI Career Chat Assistant
- ⚡ Powered by Ollama + Qwen LLM
- 🔒 Local AI Processing for improved privacy


# 🎯 Problem Statement

Students often struggle to understand how well their resumes align with industry expectations.

They may not know:

- Which skills they are missing for their target role
- Which technologies they should learn next
- Which projects can strengthen their profile
- Which certifications are relevant
- How to improve their resume
- How prepared they are for technical interviews
- Which career opportunities best match their current skills

Traditional resume analyzers generally focus on ATS scoring or resume feedback, but they do not provide a complete and personalized career development strategy.

**COGNITIVE NEXUS** addresses this problem by using a collaborative **Multi-Agent AI system** that analyzes resumes, identifies skill gaps, recommends learning resources, projects and certifications, prepares interview questions, and generates a personalized career roadmap.


# 💡 Our Solution

Cognitive Nexus transforms a simple resume into an intelligent career development plan.

The system follows an end-to-end workflow:

```text
Resume Upload
      ↓
Resume Parsing
      ↓
Skill Extraction
      ↓
Career Readiness Analysis
      ↓
Skill Gap Detection
      ↓
Learning Roadmap
      ↓
Project Recommendations
      ↓
Certification Recommendations
      ↓
Resume Improvement
      ↓
Interview Preparation
      ↓
Job Matching
      ↓
Career Report + Dashboard + AI Chat

```

# 🛠 Tech Stack

| Category             | Technologies       |
| -------------------- | ------------------ |
| Programming Language | Python             |
| LLM                  | Qwen               |
| Framework            | LangChain          |
| LLM Runtime          | Ollama             |
| Notebook Environment | Jupyter Notebook   |
| Data Processing      | Pandas, NumPy      |
| Visualization        | Matplotlib, Plotly |
| PDF Processing       | PDFPlumber, PyPDF  |
| Report Generation    | FPDF, ReportLab    |
| Vector Search        | FAISS              |
| AI Platform          | AMD AI Compute     |

## 🏗️ System Architecture

```mermaid
graph TD
    A[Resume PDF] --> B[Resume Parser Agent]
    B --> C[Skill Extraction Agent]
    C --> D[Career Readiness Agent]
    D --> E[Skill Gap Analysis Agent]

    E --> F[Learning Roadmap Agent]
    E --> G[Project Recommendation Agent]
    E --> H[Certification Recommendation Agent]

    F --> I[Resume Improver Agent]
    G --> I
    H --> I

    I --> J[Interview Preparation Agent]
    J --> K[Job Matching Agent]
    K --> L[Career Report Generator]

    L --> M[Interactive Dashboard]
    M --> N[Cognitive Nexus AI Chat]

    O[Qwen LLM] --> B
    O --> C
    O --> D
    O --> E
    O --> F
    O --> G
    O --> H
    O --> I
    O --> J
    O --> K

    P[LangChain] --> O
    Q[Ollama] --> O
    R[AMD AI Compute] --> Q
```

# 📸 Project Screenshots

## 🏠 Dashboard

<img src="assets/screenshots/dashboard (2).png" width="100%"/>

---

## 📄 Resume Analyzer

<img src="assets/screenshots/resume_upload (2).png" width="100%"/>

---

## 🤖 AI Chat

<img src="assets/screenshots/chat (2).png" width="100%"/>

---

## 📈 Placement Progress Analytics

<img src="assets/screenshots/Placement Progress Chart.png" width="100%"/>

---

## 🧠 Skills Breakdown

<img src="assets/screenshots/Skills Breakdown Chart (2).png" width="100%"/>

---

## 💡 AI Suggestions

<img src="assets/screenshots/AI Suggestions.png" width="100%"/>

---

## 📋 Daily Tasks

<img src="assets/screenshots/tasks (2).png" width="100%"/>

---

## 👤 Profile Dashboard

<img src="assets/screenshots/profile (2).png" width="100%"/>

---

## 📄 Resume Parsing Agent

<img src="assets/screenshots/resume_parser_output (2).png" width="100%"/>

---

## ⚙ Backend Running

<img src="assets/screenshots/backend (2).png" width="100%"/>

---

## 💬 Cognitive Nexus AI Conversation

<img src="assets/screenshots/Cognitive-Nexus AI Chat Interface.png" width="100%"/>


# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/AnkushRana528/Cognitive-Nexus.git

cd Cognitive-Nexus
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Start Ollama

```bash
ollama serve
```

## Pull the Model

```bash
ollama pull qwen3:4b
```

## Launch Jupyter

```bash
jupyter notebook
```

Open

```
notebooks/00_master_pipeline_(2).ipynb
```

Run all cells.

# 👥 Team

## Team Lead

**Ankush Rana**

## Team Members

- Ashish Kumar
- Saransh Arora
- Harmandeep Kaur

Institution:
Maharishi Markandeshwar (Deemed to be University)


