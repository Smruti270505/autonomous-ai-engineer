from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def improve_code(code):

    prompt = f"""
You are an expert senior software engineer.

Improve this code carefully.

Requirements:
- Keep functionality same
- Improve readability
- Improve structure
- Remove bad practices
- Return ONLY improved code
- Do not explain anything

CODE:
{code}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content