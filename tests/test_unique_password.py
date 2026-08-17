import sqlite3

connection = sqlite3.connect("database.db")
try:
    connection.execute("""insert into students(name, email, phone) values (?,?,?)""", ("test student 1", "test@example.com", "1111111111"))
    connection.execute("""insert into students(name, email, phone) values (?,?,?)""", ("test student 2", "test@example.com", "1111111112"))
    connection.commit()
    print("error: duplicate email was allowed")
except sqlite3.IntegrityError:
    print("succeess: duplicate email was blocked")
finally:
    connection.close()