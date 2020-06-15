import sqlite3

class Student:
    def __init__(self, id, first_name, surname, age):
        self.id = id
        self.first_name = first_name
        self.surname = surname
        self.age = age

    def insert_student(first_name, surname, age):
        connection = sqlite3.connect(".students.db")
        cursor = connection.cursor()
        sql = f"""
            INSERT INTO students (first_name, surname, age)
            VALUES ("{first_name}", "{surname}", {age})
        """
        cursor.execute(sql)
        connection.commit()
        connection.close()

    def get_all_students():
        connection = sqlite3.connect(".students.db")
        cursor = connection.cursor()
        sql = "SELECT * FROM students"
        rows = cursor.execute(sql)
        student_rows = rows.fetchall()
        connection.close()
        return [Student(*student_row) for student_row in student_rows]

    def student_search(surname):
        connection = sqlite3.connect(".students.db")
        cursor = connection.cursor()
        sql = f"SELECT * FROM students WHERE surname='{surname}'"
        row = cursor.execute(sql)
        student_row = row.fetchone()
        connection.close()
        if student_row is not None:
            return Student(*student_row)
        else:
            return student_row

    def update_student(id, new_age):
        connection = sqlite3.connect(".students.db")
        cursor = connection.cursor()
        sql = f"UPDATE students SET age={new_age} WHERE id={id}"
        cursor.execute(sql)
        connection.commit()
        connection.close()
