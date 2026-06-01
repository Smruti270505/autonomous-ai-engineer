
from tools.memory_store import save_action
from tools.tool_router import run_tool
from enum import Enum

class Tools(Enum):
    CREATE_FILE = 1
    LIST_FILES = 2
    TIME = 3
    RANDOM_NUMBER = 4
    DIRECTORY_INFO = 5

def execute_plan(plan, message):
    execution_logs = []
    results = []

    for tool in plan:
        if not isinstance(tool, Tools):
            raise ValueError(f"Invalid tool: {tool} ({type(tool)})")

        execution_logs.append(f"Executing {tool.name}")

        if tool == Tools.CREATE_FILE:
            filename = "agent_file.txt"
            if message and " " in message:
                parts = message.split()
                if len(parts) >= 3:
                    filename = parts[2].strip()  # Prevents potential file system errors
            try:
                results.append(run_tool(tool.name, filename, "Created by autonomous planner."))
                save_action(f"Executed create_file on {filename}")
            except Exception as e:
                save_action(f"Failed to execute create_file on {filename}: {str(e)}")

        elif tool in [Tools.LIST_FILES, Tools.TIME, Tools.RANDOM_NUMBER, Tools.DIRECTORY_INFO]:
            try:
                result = run_tool(tool.name)
                results.append(result)
                save_action(f"Executed {tool.name}")
            except Exception as e:
                save_action(f"Failed to execute {tool.name}: {str(e)}")

    execution_text = "\n".join(execution_logs)
    final_output = (
        "[Execution]\n"
        + execution_text
        + "\n\n[Results]\n"
        + "\n".join(results)
    )

    return final_output
