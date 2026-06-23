import ast

def check_syntax(filepath):

    try:

        with open(
            filepath,
            "r",
            encoding="utf-8"
        ) as f:

            code = f.read()

        ast.parse(code)

        return "Syntax OK"

    except Exception as e:

        return str(e)