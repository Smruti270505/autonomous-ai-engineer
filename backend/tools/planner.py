from tools.intent_detector import detect_tool

def create_plan(message):

    message = message.lower()

    plan = []

    if "create file" in message:
        plan.append("create_file")

    if "list files" in message:
        plan.append("list_files")

    if "time" in message:
        plan.append("time")

    if "random number" in message:
        plan.append("random_number")

    if "directory info" in message:
        plan.append("directory_info")

    return plan