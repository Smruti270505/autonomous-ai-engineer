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
    return None