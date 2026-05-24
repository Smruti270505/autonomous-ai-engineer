from tools.tool_router import run_tool

def execute_plan(plan, message):

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

        # LIST FILES
        elif tool == "list_files":

            result = run_tool(
                "list_files"
            )

            results.append(result)

        # TIME
        elif tool == "time":

            result = run_tool(
                "time"
            )

            results.append(result)

        # RANDOM NUMBER
        elif tool == "random_number":

            result = run_tool(
                "random_number"
            )

            results.append(result)

        # DIRECTORY INFO
        elif tool == "directory_info":

            result = run_tool(
                "directory_info"
            )

            results.append(result)

    return "\n\n".join(results)