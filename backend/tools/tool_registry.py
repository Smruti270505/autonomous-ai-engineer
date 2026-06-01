from tools.error_runner import run_python_file
from tools.self_heal import self_heal
from tools.debug_analyzer import analyze_bugs
from tools.bug_fixer import fix_bugs
from tools.code_editor import overwrite_code
from tools.code_improver import improve_code
from tools.code_reader import read_code_file
from tools.code_summarizer import summarize_code
from tools.project_scanner import scan_project
from tools.project_analyzer import analyze_project
from tools.history_tool import show_history
from tools.terminal_tool import run_command
from tools.update_file_tool import update_file
from tools.rename_file_tool import rename_file
from tools.directory_info_tool import directory_info
from tools.echo_tool import echo
from tools.random_tool import random_number
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
    },
        "update_file": {
        "function": update_file,
        "description": "Updates existing files",
        "usage": "update file test.py"
    },

    "rename_file": {
        "function": rename_file,
        "description": "Renames files",
        "usage": "rename file old.py new.py"
    },

    "directory_info": {
        "function": directory_info,
        "description": "Returns folder information",
        "usage": "directory info"
    },

    "echo": {
        "function": echo,
        "description": "Repeats user message",
        "usage": "echo hello"
    },

    "random_number": {
        "function": random_number,
        "description": "Generates random number",
        "usage": "random number"
    },
        "run_command": {
        "function": run_command,
        "description": "Executes terminal commands",
        "usage": "run command dir"
    },
        "history": {
        "function": show_history,
        "description": "Shows agent action history",
        "usage": "show history"
    },
        "scan_project": {
        "function": scan_project,
        "description": "Scans project structure",
        "usage": "scan project"
    },

    "analyze_project": {
        "function": analyze_project,
        "description": "Analyzes project architecture",
        "usage": "analyze project"
    },
        "read_code_file": {
        "function": read_code_file,
        "description": "Reads source code files",
        "usage": "read code backend/main.py"
    },

    "summarize_code": {
        "function": summarize_code,
        "description": "Summarizes source code",
        "usage": "summarize code backend/main.py"
    },
        "overwrite_code": {
        "function": overwrite_code,
        "description": "Overwrites source code files",
        "usage": "overwrite code main.py"
    },

    "improve_code": {
        "function": improve_code,
        "description": "Improves source code intelligently",
        "usage": "improve code main.py"
    },
        "analyze_bugs": {
        "function": analyze_bugs,
        "description": "Analyzes code for bugs",
        "usage": "analyze bugs tools/executor.py"
    },

    "fix_bugs": {
        "function": fix_bugs,
        "description": "Fixes bugs automatically",
        "usage": "fix bugs tools/executor.py"
    },
        "run_python_file": {
        "function": run_python_file,
        "description": "Runs Python files and captures errors",
        "usage": "run python main.py"
    },

    "self_heal": {
        "function": self_heal,
        "description": "Automatically fixes broken Python files",
        "usage": "self heal main.py"
    }
}