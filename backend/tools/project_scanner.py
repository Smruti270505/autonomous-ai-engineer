import os

def scan_project():

    project_data = []

    for root, dirs, files in os.walk("."):

        for file in files:

            if "venv" in root:
                continue

            path = os.path.join(root, file)

            project_data.append(path)

    return "\n".join(project_data)