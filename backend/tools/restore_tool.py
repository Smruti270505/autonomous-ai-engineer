import os
import shutil

def restore_backup(filename):

    backup_path = os.path.join(
        "backups",
        filename + ".bak"
    )

    original_path = filename

    if not os.path.exists(backup_path):
        return "Backup not found."

    shutil.copy(
        backup_path,
        original_path
    )

    return "Backup restored."