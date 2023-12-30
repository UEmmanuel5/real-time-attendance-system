import mysql.connector

def connect_to_db():
    return mysql.connector.connect(host="localhost",user="root",password="10Hidden@4rmall", database="attendance")

def insert_to_db(insert_query,data_to_insert):
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute(insert_query, data_to_insert)
    connection.commit()
    cursor.close()
    connection.close()

def query_database(query, check_data):
   pass




def mark_attendance(student_id, course,date):
    query = "INSERT INTO attendances (student_id,course,date) VALUES (%s,%s,%s)"
    data = (student_id, course, date)
    insert_to_db(query, data)
    print("Attendance marked")

def is_attendance_marked(student_id,course,date):
    query = "select student_id from attendances where student_id = %s and course = %s and DATE(date) = DATE(%s)"
    check_data = (student_id, course, date)
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute(query, check_data)
    
    result = cursor.fetchone()
    if (result):
        return True
    else:
        return False
