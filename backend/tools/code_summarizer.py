from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def summarize_code(code):

    prompt = f"""
You are an expert software engineer.

Analyze this code carefully.

Explain:
1. What this code does
2. Main functionality
3. Important logic
4. Technologies used
5. Possible improvements

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
