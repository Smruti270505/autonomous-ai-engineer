```python
from tools.memory_store import save_action
from tools.tool_router import run_tool
from enum import Enum

class Tools(Enum):
    create_file = 1
    list_files = 2
    time = 3
    random_number = 4
    directory_info = 5

def execute_plan(plan, message):
    execution_logs = []
    results = []

    for tool in plan:
        if not isinstance(tool, Tools):
            raise ValueError(f"Invalid tool: {tool}")

        tool_name = tool.name.lower()
        execution_logs.append(f"Executing {tool_name}")

        if tool_name == "create_file":
            parts = message.split()
            filename = "agent_file.txt"
            if len(parts) >= 3:
                filename = parts[2]
            results.append(run_tool(tool_name, filename, "Created by autonomous planner."))
            save_action(f"Executed create_file on {filename}")

        elif tool_name in ["list_files", "time", "random_number", "directory_info"]:
            result = run_tool(tool_name)
            results.append(result)
            save_action(f"Executed {tool_name}")

    execution_text = "\n".join(execution_logs)
    final_output = (
        "[Execution]\n"
        + execution_text
        + "\n\n[Results]\n"
        + "\n\n".join(results)
    )

    return final_output
```