from os import path
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

def restore_database(backup_path):
    database_path = Path("student_management.db")
    if not backup_path.exists():
        raise FileNotFoundError("backup file not found.")
    shutil.copy2(backup_path, database_path)
    print("database restored successfully.")

