import os

def update_file(filename, content):

    path = os.path.join(
        "generated",
        filename
    )

    if not os.path.exists(path):
        return "File does not exist."

    with open(path, "w") as file:
        file.write(content)

    return f"{filename} updated successfully."