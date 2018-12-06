from mysql.connector import connect


db = connect(host= 'localhost', user='root', passwd= '', database= 'python_db')

cursor = db.cursor()
# sql injection

sql = "insert into students values (null, 'Mary Jane', 'jane@yahoo.com', '1999-07-7', 'Female', 4)"

cursor.execute(sql)

db.commit()
