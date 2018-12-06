from mysql.connector import connect


db = connect(host= 'localhost', user='root', passwd= '', database= 'school')

cursor = db.cursor()

sql = "SELECT * FROM employees WHERE salary< (SELECT AVG(salary) FROM employees)"

cursor.execute(sql)

data = cursor.fetchall()

print(data)

for item in data:
    print(item [0], item [1], item [3])