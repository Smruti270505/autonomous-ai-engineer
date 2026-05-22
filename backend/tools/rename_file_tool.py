import os

def rename_file(old_name, new_name):

    old_path = os.path.join(
        "generated",
        old_name
    )

    new_path = os.path.join(
        "generated",
        new_name
    )

    if not os.path.exists(old_path):
        return "File does not exist."

    os.rename(old_path, new_path)

    return f"{old_name} renamed to {new_name}"