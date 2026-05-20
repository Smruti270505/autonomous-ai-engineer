import os

def list_files():

    folder = "generated"

    if not os.path.exists(folder):
        return "No generated folder found."

    files = os.listdir(folder)

    if not files:
        return "No files available."

    return "\n".join(files)