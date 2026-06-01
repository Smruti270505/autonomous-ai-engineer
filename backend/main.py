from tools.ai_planner import generate_plan
from tools.reasoning_engine import generate_reasoning
from tools.executor import execute_plan
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
    ai_plan = generate_plan(
        latest_message
    )

    try:

        plan = eval(ai_plan)

    except:

        plan = []
    reasoning = generate_reasoning(plan)
    if len(plan) > 1:
     

        result = execute_plan(
            plan,
            latest_message
        )

        final_response = (
            "[Reasoning]\n"
            + reasoning
            + "\n\n"
            + result
        )

        return {
            "response": final_response
        }
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
        # UPDATE FILE TOOL
    if detected_tool == "update_file":

        parts = latest_message.split()

        filename = parts[2]

        result = run_tool(
            "update_file",
            filename,
            "Updated by AI agent."
        )

        return {
            "response": result
        }

    # RENAME FILE TOOL
    if detected_tool == "rename_file":

        parts = latest_message.split()

        old_name = parts[2]
        new_name = parts[3]

        result = run_tool(
            "rename_file",
            old_name,
            new_name
        )

        return {
            "response": result
        }

    # DIRECTORY INFO TOOL
    if detected_tool == "directory_info":

        result = run_tool(
            "directory_info"
        )

        return {
            "response": result
        }

    # ECHO TOOL
    if detected_tool == "echo":

        text = latest_message.replace(
            "echo",
            ""
        )

        result = run_tool(
            "echo",
            text
        )

        return {
            "response": result
        }

    # RANDOM NUMBER TOOL
    if detected_tool == "random_number":

        result = run_tool(
            "random_number"
        )

        return {
            "response": result
        }
        # TERMINAL TOOL
    if detected_tool == "run_command":

        command = latest_message.replace(
            "run command",
            ""
        ).strip()

        result = run_tool(
            "run_command",
            command
        )

        return {
            "response": result
        }
        # HISTORY TOOL
    if detected_tool == "history":

        result = run_tool(
            "history"
        )

        return {
            "response": result
        }
        # SCAN PROJECT TOOL
    if detected_tool == "scan_project":

        result = run_tool(
            "scan_project"
        )

        return {
            "response": result
        }

    # ANALYZE PROJECT TOOL
    if detected_tool == "analyze_project":

        project_structure = run_tool(
            "scan_project"
        )

        result = run_tool(
            "analyze_project",
            project_structure
        )

        return {
            "response": result
        }
        # READ CODE TOOL
    if detected_tool == "read_code_file":

        parts = latest_message.split()

        filepath = parts[2]

        result = run_tool(
            "read_code_file",
            filepath
        )

        return {
            "response": result
        }

    # SUMMARIZE CODE TOOL
    if detected_tool == "summarize_code":

        parts = latest_message.split()

        filepath = parts[2]

        code = run_tool(
            "read_code_file",
            filepath
        )

        result = run_tool(
            "summarize_code",
            code
        )

        return {
            "response": result
        }
        # IMPROVE CODE TOOL
    if detected_tool == "improve_code":

        parts = latest_message.split()

        filepath = parts[2]

        original_code = run_tool(
            "read_code_file",
            filepath
        )

        improved_code = run_tool(
            "improve_code",
            original_code
        )

        result = run_tool(
            "overwrite_code",
            filepath,
            improved_code
        )

        return {
            "response": (
                result
                + "\n\nCode improved successfully."
            )
        }
        # ANALYZE BUGS TOOL
    if detected_tool == "analyze_bugs":

        parts = latest_message.split()

        filepath = parts[-1]

        code = run_tool(
            "read_code_file",
            filepath
        )

        result = run_tool(
            "analyze_bugs",
            code
        )

        return {
            "response": result
        }

    # FIX BUGS TOOL
    if detected_tool == "fix_bugs":

        parts = latest_message.split()

        filepath = parts[-1]

        original_code = run_tool(
            "read_code_file",
            filepath
        )

        fixed_code = run_tool(
            "fix_bugs",
            original_code
        )

        overwrite_result = run_tool(
            "overwrite_code",
            filepath,
            fixed_code
        )

        return {
            "response":
            overwrite_result
            + "\n\nBugs fixed successfully."
        }
        # SELF HEAL TOOL
    if detected_tool == "self_heal":

        parts = latest_message.split()

        filepath = parts[-1]

        result = run_tool(
            "self_heal",
            filepath
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