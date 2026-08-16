import sqlite3

database_name = "student_management.db"

def get_connection():
    try:
        connection = sqlite3.connect(database_name)
        return connection
    except sqlite3.error as error:
        print("database connection error: ", error)
        return None

def create_student_table():
    connection = get_connection()
    if connection is None:
        return
    cursor = connection.cursor()
    cursor.execute("""create table if not exists students (student_id integer primary key, name text not null, email text, phone text)""")
    connection.commit()
    connection.close()

if __name__ == "__main__":
    create_student_table()
    print("sqlite database and students table created successfully")