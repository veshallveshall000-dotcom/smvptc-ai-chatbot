import os
from groq import Groq
import logging

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_ai_response(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1024
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        logging.error(f"Groq error: {e}")
        return "AI response failed (Groq)."
