
import requests
import os

GROQ_API_KEY = "gsk_H8r5fpIMcQsi91VefnrDWGdyb3FYzv2mK1e3MYwvmIBeAs8GCpV"

def generate_answer(context, query):
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""
Answer ONLY using the context below.
If the answer is not in the context, say "Not found".

Context:
{context}

Question:
{query}
"""

    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    return response.json()["choices"][0]["message"]["content"]