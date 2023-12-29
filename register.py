from db import connect_to_db

connection = connect_to_db()

def register_student():
    studentID = input("Enter you student Number: ")
    studentName = input("Enter your name: ")

    cursor = connection.cursor()
    insert_query = "INSERT INTO students (student_number, student_name) VALUES (%s, %s)"
    data_to_insert = (studentID,studentName)
    cursor.execute(insert_query, data_to_insert)
    connection.commit()
    cursor.close()
    connection.close()

    print("{} information saved".format(studentName))
    

if __name__ == '__main__':
    register_student()