

def self_heal(filepath):
    from tools.tool_registry import TOOLS

    logs = []

    for attempt in range(3):

        logs.append(
            f"Attempt {attempt + 1}"
        )

        result = TOOLS[
            "run_python_file"
        ]["function"](filepath)

        # SUCCESS
        if result["success"]:

            logs.append(
                "Execution successful"
            )

            logs.append(
                result["output"]
            )

            return "\n\n".join(logs)

        # FAILURE
        logs.append(
            "Execution failed"
        )

        logs.append(
            result["output"]
        )

        # READ FILE
        code = TOOLS[
            "read_code_file"
        ]["function"](filepath)

        # FIX BUGS
        fixed_code = TOOLS[
            "fix_bugs"
        ]["function"](code)

        # OVERWRITE FILE
        overwrite_result = TOOLS[
            "overwrite_code"
        ]["function"](
            filepath,
            fixed_code
        )

        logs.append(
            overwrite_result
        )

    logs.append(
        "Failed after maximum retries"
    )

    return "\n\n".join(logs)