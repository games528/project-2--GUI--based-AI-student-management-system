import sqlite3
import os
base_dir = os.path.dirname(os.path.abspath(__file__))
database_name = os.path.join(base_dir,"student_management.db") 

def get_connection():
    try:
        connection = sqlite3.connect(database_name)
        connection.execute("pragma foreign_keys = ON")
        return connection
    except sqlite3.error as error:
        print("database connection error: ", error)
        return None

def create_student_table():
    connection = get_connection()
    if connection is None:
        return
    cursor = connection.cursor()
    cursor.execute("""create table if not exists students (student_id integer primary key autoincrement, name text not null, email text not null unique, phone text not null check(length(phone) = 10))""")
    connection.commit()
    connection.close()

def create_academic_records_table():
    connection  = get_connection()
    if connection is None:
        return
    cursor = connection.cursor()
    cursor.execute("""create table if not exists academic_records (record_id integer primary key autoincrement, student_id integer not null, subject text not null, marks integer, foreign key(student_id) references students(student_id))""")
    connection.commit()
    connection.close()

def add_student(name, email, phone):
    connection = get_connection()
    if connection is None:
        return False
    cursor = connection.cursor()
    cursor.execute(""" insert into students (name, email, phone) values (?,?,?) """, (name, email, phone))
    connection.commit()
    connection.close()
    return True

def get_students():
    connection = get_connection()
    if connection is None:
        return []
    cursor = connection.cursor()
    cursor.execute("select * from students")
    students = cursor.fetchall()
    connection.close()
    return students

def update_students(student_id, name, email, phone):
    connection = get_connection()
    if connection is None:
        return False
    cursor = connection.cursor()
    cursor.execute(""" update students set name = ?, email = ?, phone = ? where student_id = ? """, (name, email, phone, student_id))
    connection.commit()
    updated = cursor.rowcount > 0
    connection.close()
    return updated

def delete_student(student_id):
    connection = get_connection()
    if connection is None:
        return False
    cursor = connection.cursor()
    cursor.execute("delete from students where student_id = ?", (student_id,))
    connection.commit()
    deleted = cursor.rowcount > 0
    connection.close()
    return deleted

def add_gender_column():
    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    cursor.execute(
        "PRAGMA table_info(students)"
    )

    columns = cursor.fetchall()

    column_names = [column[1] for column in columns]

    if "gender" not in column_names:
        cursor.execute(
            "ALTER TABLE students ADD COLUMN gender TEXT"
        )

        connection.commit()

    connection.close()

def get_boys_count():
    connection = get_connection()

    if connection is None:
        return 0

    cursor = connection.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM students WHERE gender = ?",
        ("Male",)
    )

    count = cursor.fetchone()[0]

    connection.close()

    return count


def get_girls_count():
    connection = get_connection()

    if connection is None:
        return 0

    cursor = connection.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM students WHERE gender = ?",
        ("Female",)
    )

    count = cursor.fetchone()[0]

    connection.close()

    return count

def create_attendance_table():
    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance_records (
            attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            date TEXT NOT NULL,
            status TEXT NOT NULL,
            FOREIGN KEY(student_id) REFERENCES students(student_id)
        )
    """)

    connection.commit()
    connection.close()

def get_average_attendance():
    connection = get_connection()

    if connection is None:
        return 0

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            CASE
                WHEN COUNT(*) = 0 THEN 0
                ELSE
                    (SUM(
                        CASE
                            WHEN status = 'Present' THEN 1
                            ELSE 0
                        END
                    ) * 100.0) / COUNT(*)
            END
        FROM attendance_records
    """)

    average = cursor.fetchone()[0]

    connection.close()

    return round(average, 2)

