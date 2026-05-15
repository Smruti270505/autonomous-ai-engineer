from tools.file_tool import create_file
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from groq import Groq
from dotenv import load_dotenv
from pydantic import BaseModel
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: list[Message]

@app.get("/")
def home():
    return {"message": "AI Backend Running"}

@app.post("/chat")
def chat(data: ChatRequest):

    latest_message = data.messages[-1].content.lower()

    if "create file" in latest_message or "create a file" in latest_message:

        parts = latest_message.split()

        filename = "new_file.txt"

        if len(parts) >= 3:
            filename = parts[2]

        result = create_file(
            filename,
            "This file was created by AI agent."
        )

        return {
            "response": result
        }

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": msg.role,
                "content": msg.content
            }
            for msg in data.messages
        ]
    )

    ai_reply = response.choices[0].message.content

    return {
        "response": ai_reply
    }