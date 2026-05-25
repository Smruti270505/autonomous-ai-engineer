from tools.memory_store import save_action
from tools.tool_router import run_tool

execution_logs = []

def execute_plan(plan, message):

    execution_logs.clear()

    results = []

    for tool in plan:

        # CREATE FILE
        if tool == "create_file":

            parts = message.split()

            filename = "agent_file.txt"

            if len(parts) >= 3:
                filename = parts[2]

            result = run_tool(
                "create_file",
                filename,
                "Created by autonomous planner."
            )

            results.append(result)

            execution_logs.append(
                "Executed create_file"
            )

            save_action(
                f"Executed create_file on {filename}"
            )

        # LIST FILES
        elif tool == "list_files":

            result = run_tool(
                "list_files"
            )

            results.append(result)

            execution_logs.append(
                "Executed list_files"
            )

            save_action(
                "Executed list_files"
            )

        # TIME
        elif tool == "time":

            result = run_tool(
                "time"
            )

            results.append(result)

            execution_logs.append(
                "Executed time"
            )

            save_action(
                "Executed time tool"
            )

        # RANDOM NUMBER
        elif tool == "random_number":

            result = run_tool(
                "random_number"
            )

            results.append(result)

            execution_logs.append(
                "Executed random_number"
            )

            save_action(
                "Executed random_number"
            )

        # DIRECTORY INFO
        elif tool == "directory_info":

            result = run_tool(
                "directory_info"
            )

            results.append(result)

            execution_logs.append(
                "Executed directory_info"
            )

            save_action(
                "Executed directory_info"
            )

    execution_text = "\n".join(execution_logs)

    final_output = (
        "[Execution]\n"
        + execution_text
        + "\n\n[Results]\n"
        + "\n\n".join(results)
    )

    return final_output