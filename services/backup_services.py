from pathlib import Path
import shutil
import os
from datetime import datetime
import sqlite3

# Path to your actual SQLite database file
DB_PATH = "student_management.db"

# Path to your backups folder
BACKUP_DIR = "backups/"

def backup_database():
    # Check if the database file actually exists before trying to copy it
    if not os.path.exists(DB_PATH):
        raise FileNotFoundError("Database file not found. Cannot create backup.")

    # Make sure the backups folder exists (create it if somehow missing)
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

    # We'll build this filename properly in Step 3 — placeholder for now
    backup_filename = "temp_backup.db"
    backup_path = os.path.join(BACKUP_DIR, backup_filename)

    # This is the actual copy operation
    shutil.copy2(DB_PATH, backup_path)

    return backup_path

if __name__ == "__main__":
    backup_folder = Path("exports/backups")
    backup_files = list(backup_folder.glob("*.db"))
    if backup_files:
        latest_backup = max(backup_files, key=lambda file: file.stat().st_mtime)
        print("latest backup:", latest_backup)
        connection = sqlite3.connect(latest_backup)
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()
        print("tables in backup: ")
        for table in tables:
            print(table[0])
        connection.close()
else:
    print("no backup files found.")