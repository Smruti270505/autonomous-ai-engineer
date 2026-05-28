import os

BASE_DIR = os.path.dirname(
    os.path.dirname(__file__)
)

def read_code_file(filepath):

    full_path = os.path.join(
        BASE_DIR,
        filepath
    )

    if not os.path.exists(full_path):
        return "File does not exist."

    try:

        with open(
            full_path,
            "r",
            encoding="utf-8"
        ) as file:

            content = file.read()

        return content

    except Exception as error:

        return str(error)