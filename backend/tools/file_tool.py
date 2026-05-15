if "create file" in latest_message or "create a file" in latest_message:

    parts = latest_message.split()

    filename = "new_file.txt"

    if len(parts) >= 4:
        filename = parts[3]

    elif len(parts) >= 3:
        filename = parts[2]

    result = create_file(
        filename,
        "This file was created by AI agent."
    )

    return {
        "response": result
    }