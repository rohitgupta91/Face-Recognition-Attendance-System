import mysql.connector

conn = mysql.connector.connect(username='root', password='R9140hit@',host='localhost',database='face_recognition')
cursor = conn.cursor()

cursor.execute("show databases")

data = cursor.fetchall()

print(data)

conn.close()