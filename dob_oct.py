from mysql.connector import connect


db = connect(host= 'localhost', user='root', passwd= '', database= 'school')

cursor = db.cursor()

sql = "select names, dob from employees where month (dob)=10"

cursor.execute(sql)

data = cursor.fetchall()

print(data)