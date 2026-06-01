from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def fix_bugs(code):

    prompt = f"""
You are an expert Python debugger.

Your task is to fix ONLY the specific bug.

STRICT RULES:
- Preserve ALL original code
- Do NOT rewrite the entire file
- Change ONLY broken lines
- Keep edits minimal
- Do NOT add new functionality
- Do NOT add explanations
- Do NOT generate example projects
- Return ONLY corrected code
- Keep the code almost identical

BROKEN CODE:
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

    result = response.choices[0].message.content

    result = result.replace(
        "```python",
        ""
    )

    result = result.replace(
        "```",
        ""
    )

    result = result.strip()

    return result