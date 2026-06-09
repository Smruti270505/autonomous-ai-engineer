import os
import re

def dependency_mapper():

    dependencies = []

    for root, dirs, files in os.walk("."):

        # Skip huge folders
        dirs[:] = [
            d for d in dirs
            if d not in [
                "venv",
                "__pycache__",
                ".git",
                "node_modules",
                ".next"
            ]
        ]

        for file in files:

            if not file.endswith(".py"):
                continue

            filepath = os.path.join(
                root,
                file
            )

            try:

                with open(
                    filepath,
                    "r",
                    encoding="utf-8"
                ) as f:

                    content = f.read()

                imports = re.findall(
                    r"^(?:from|import)\s+(.+)",
                    content,
                    re.MULTILINE
                )

                dependencies.append(
                    f"\n{filepath}"
                )

                for imp in imports:

                    dependencies.append(
                        f"   -> {imp}"
                    )

            except Exception:
                pass

    return "\n".join(
        dependencies
    )