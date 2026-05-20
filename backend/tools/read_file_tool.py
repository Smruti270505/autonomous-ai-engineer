import os

def read_file(filename):

    path = os.path.join(
        "generated",
        filename
    )

    if not os.path.exists(path):
        return "File does not exist."

    with open(path, "r") as file:
        content = file.read()

    return content