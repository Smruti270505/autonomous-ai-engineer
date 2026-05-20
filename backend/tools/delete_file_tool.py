import os

def delete_file(filename):

    path = os.path.join(
        "generated",
        filename
    )

    if not os.path.exists(path):
        return "File does not exist."

    os.remove(path)

    return f"{filename} deleted successfully."