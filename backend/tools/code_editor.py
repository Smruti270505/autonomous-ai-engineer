import os

def overwrite_code(filepath, new_code):

    full_path = os.path.join(
        os.path.dirname(
            os.path.dirname(__file__)
        ),
        filepath
    )

    if not os.path.exists(full_path):
        return "File does not exist."

    try:

        with open(
            full_path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(new_code)

        return f"{filepath} updated successfully."

    except Exception as error:

        return str(error)