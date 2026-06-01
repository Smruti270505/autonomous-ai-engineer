from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def analyze_bugs(code):

    prompt = f"""
You are an expert debugging engineer.

Analyze this code carefully.

Tasks:
1. Detect bugs
2. Detect bad practices
3. Detect risky logic
4. Explain issues clearly

Return debugging report only.

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