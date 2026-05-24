from tools.tool_router import run_tool

def execute_workflow(message):

    results = []

    # CREATE FILE
    if "create file" in message:

        parts = message.split()

        filename = "workflow.txt"

        if len(parts) >= 3:
            filename = parts[2]

        result = run_tool(
            "create_file",
            filename,
            "Created from workflow engine."
        )

        results.append(result)

    # LIST FILES
    if "list files" in message:

        result = run_tool(
            "list_files"
        )

        results.append(result)

    # TIME
    if "time" in message:

        result = run_tool(
            "time"
        )

        results.append(result)

    return "\n\n".join(results)