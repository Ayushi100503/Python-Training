import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='Aayyuusshhii@01',
    database='company_db')
cursor = conn.cursor()
cursor.execute("select * from employees")

rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
conn.close()