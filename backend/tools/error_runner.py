import subprocess

def run_python_file(filepath):

    try:

        result = subprocess.check_output(
            ["python", filepath],
            stderr=subprocess.STDOUT,
            text=True
        )

        return {
            "success": True,
            "output": result
        }

    except subprocess.CalledProcessError as error:

        return {
            "success": False,
            "output": error.output
        }