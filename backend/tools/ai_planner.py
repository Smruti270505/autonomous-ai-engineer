from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

AVAILABLE_TOOLS = [
    "create_file",
    "list_files",
    "time",
    "random_number",
    "directory_info",
    "read_code_file",
    "summarize_code"
]

def generate_plan(message):

    prompt = f"""
You are an AI planning engine.

Available tools:
{AVAILABLE_TOOLS}

User request:
{message}
You must choose tools carefully.

Rules:
- If user wants to READ source code → use read_code_file
- If user wants code explanation/analysis → use summarize_code
- If user wants file creation → use create_file
- Never confuse reading with creating
- Return ONLY a Python list

Example:
["read_code_file"]Return ONLY a Python list of tool names.

Example:
["create_file", "list_files"]
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

    return result