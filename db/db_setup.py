import sqlite3

class DBSetup:
    def __init__(self):
        pass

    def set_up_table():
        connection = sqlite3.connect(".students.db")
        cursor = connection.cursor()
        cursor.execute("DROP TABLE IF EXISTS students")
        cursor.execute("""
          CREATE TABLE students (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            surname TEXT,
            age INTEGER
          )
        """)
        connection.commit()
        connection.close()
