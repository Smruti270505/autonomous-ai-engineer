from tools.read_file_tool import read_file
from tools.list_files_tool import list_files
from tools.delete_file_tool import delete_file
from tools.time_tool import get_current_time
from tools.file_tool import create_file
from tools.math_tool import calculate

TOOLS = {
    "create_file": {
        "function": create_file,
        "description": "Creates files dynamically"
    },

    "calculate": {
        "function": calculate,
        "description": "Performs mathematical calculations"
    },
     "time": {
        "function": get_current_time,
        "description": "Returns current system time",
        "usage": "what is the time"
    },
        "read_file": {
        "function": read_file,
        "description": "Reads file contents",
        "usage": "read file test.py"
    },

    "list_files": {
        "function": list_files,
        "description": "Lists generated files",
        "usage": "list files"
    },

    "delete_file": {
        "function": delete_file,
        "description": "Deletes a file",
        "usage": "delete file test.py"
    }
}