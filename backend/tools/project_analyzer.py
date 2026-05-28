from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def analyze_project(project_structure):

    prompt = f"""
You are an expert AI software architect.

Analyze this project structure:

{project_structure}

Explain:
1. What type of project this is
2. Main architecture
3. Strengths
4. Possible future improvements
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