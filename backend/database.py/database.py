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
    cursor.execute("""create table if not exists students (student_id integer primary key autoincrement, name text not null, email text not null unique, phone text not null check(length(phone) = 10))""")
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

