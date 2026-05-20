from tools.intent_detector import detect_tool
from tools.tool_router import run_tool
from tools.tool_registry import TOOLS
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
    detected_tool = detect_tool(latest_message)
    if "what tools" in latest_message or "available tools" in latest_message:

        tool_list = []

        for tool_name, tool_data in TOOLS.items():

            description = tool_data["description"]

            tool_list.append(
                f"{tool_name} - {description}"
            )

        return {
            "response": "\n".join(tool_list)
        }

    
          # CREATE FILE TOOL
    if detected_tool == "create_file":

        parts = latest_message.split()

        filename = "new_file.txt"

        if "create a file" in latest_message and len(parts) >= 4:
            filename = parts[3]

        elif "create file" in latest_message and len(parts) >= 3:
            filename = parts[2]

        result = run_tool(
            "create_file",
            filename,
            "This file was created by AI agent."
        )

        return {
            "response": result
        }
    # CALCULATE TOOL
    if detected_tool == "calculate":

        expression = latest_message.replace(
            "calculate",
            ""
        )

        result = run_tool(
            "calculate",
            expression
        )

        return {
            "response": result
        }
    # TIME TOOL
    if detected_tool == "time":

        result = run_tool("time")

        return {
            "response": result
        }
        # READ FILE TOOL
    if detected_tool == "read_file":

        parts = latest_message.split()

        filename = parts[-1]

        result = run_tool(
            "read_file",
            filename
        )

        return {
            "response": result
        }

    # LIST FILES TOOL
    if detected_tool == "list_files":

        result = run_tool("list_files")

        return {
            "response": result
        }

    # DELETE FILE TOOL
    if detected_tool == "delete_file":

        parts = latest_message.split()

        filename = parts[-1]

        result = run_tool(
            "delete_file",
            filename
        )

        return {
            "response": result
        }
    # NORMAL AI CHAT
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