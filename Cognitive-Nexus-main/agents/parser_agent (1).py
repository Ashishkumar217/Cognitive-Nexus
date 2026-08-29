from docx import Document

def extract_text_from_pdf(path):
    try:
        text = ""
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\\n"
        return text.strip()
    except Exception:
        return ""

def extract_text_from_docx(path):
    try:
        doc = Document(path)
        return "\\n".join([p.text for p in doc.paragraphs]).strip()
    except Exception:
        return ""

def extract_resume_text(path):
    if path.lower().endswith(".pdf"):
        return extract_text_from_pdf(path)
    elif path.lower().endswith(".docx"):
        return extract_text_from_docx(path)
    return ""
''')