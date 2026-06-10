import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root123",
        database="student_system"
    )

    print("Connected successfully!")
    conn.close()
except Exception as e:
    print("Error:", e)