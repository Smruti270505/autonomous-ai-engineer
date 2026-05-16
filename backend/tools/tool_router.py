from tools.tool_registry import TOOLS

def run_tool(tool_name, *args):

    if tool_name not in TOOLS:
        return "Tool not found."

    tool_function = TOOLS[tool_name]["function"]

    return tool_function(*args)