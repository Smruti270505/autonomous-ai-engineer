def detect_tool(message):

    message = message.lower()

    if "calculate" in message:
        return "calculate"

    if "create file" in message:
        return "create_file"

    if "create a file" in message:
        return "create_file"

    return None