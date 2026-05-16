import os

def create_file(filename, content):

    os.makedirs("generated", exist_ok=True)

    path = os.path.join("generated", filename)

    with open(path, "w") as file:
        file.write(content)

    return f"File '{filename}' created successfully."