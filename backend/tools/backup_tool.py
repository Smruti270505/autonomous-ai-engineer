import os
import shutil

def create_backup(filepath):

    if not os.path.exists(filepath):
        return "File not found."

    os.makedirs("backups", exist_ok=True)

    filename = os.path.basename(filepath)

    backup_path = os.path.join(
        "backups",
        filename + ".bak"
    )

    shutil.copy(
        filepath,
        backup_path
    )

    return f"Backup created: {backup_path}"