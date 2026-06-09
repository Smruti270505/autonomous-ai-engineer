def detect_tool(message):

    message = message.lower()

    if "calculate" in message:
        return "calculate"

    if "create file" in message:
        return "create_file"

    if "create a file" in message:
        return "create_file"
    if "time" in message:
        return "time"
    if "read file" in message:
        return "read_file"

    if "list files" in message:
        return "list_files"

    if "delete file" in message:
        return "delete_file"
    if "update file" in message:
        return "update_file"

    if "rename file" in message:
        return "rename_file"

    if "directory info" in message:
        return "directory_info"

    if "echo" in message:
        return "echo"

    if "random number" in message:
        return "random_number"
    if "run command" in message:
        return "run_command"
    if "show history" in message:
        return "history"
    if "scan project" in message:
        return "scan_project"

    if "analyze project" in message:
        return "analyze_project"
    if "read code" in message:
        return "read_code_file"

    if "summarize code" in message:
        return "summarize_code"
    if "improve code" in message:
        return "improve_code"
    if "analyze bugs" in message:
        return "analyze_bugs"

    if "fix bugs" in message:
        return "fix_bugs"

    if "debug file" in message:
        return "fix_bugs"
    if "self heal" in message:
        return "self_heal"
    if "store memory" in message:
        return "store_memory"

    if "search memory" in message:
        return "search_memory"
    if "multi agent" in message:
        return "multi_agent"
    if "dependency map" in message:
        return "dependency_mapper"
    return None