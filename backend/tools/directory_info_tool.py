import os

def directory_info():

    folder = "generated"

    if not os.path.exists(folder):
        return "Generated folder does not exist."

    files = os.listdir(folder)

    total_files = len(files)

    return f"Total files: {total_files}"