OLLAMA_MODEL = "qwen3.5:4b"

def call_llm(prompt, model=OLLAMA_MODEL, temperature=0.5, max_tokens=400, think=False):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": model, "prompt": prompt, "stream": False, "think": think,
                "options": {"temperature": temperature, "num_predict": max_tokens}
            },
            timeout=90
        )
        return response.json().get("response", "").strip()
    except Exception as e:
        return f"LLM call failed: {e}"
''')