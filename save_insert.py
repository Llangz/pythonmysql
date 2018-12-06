from mysql.connector import connect


db = connect(host= 'localhost', user='root', passwd= '', database= 'python_db')

cursor = db.cursor()

# to avoid sql injection
data = ('', 'Mary Jane', 'jane@yahoo.com', '1999-07-7', 'Female', 4)

sql = "insert into students values (%s, %s, %s, %s, %s, %s)"


# dynamic binding mitigates against sql injection
cursor.execute(sql, data)

db.commit()