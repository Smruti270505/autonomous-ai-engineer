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
    return None