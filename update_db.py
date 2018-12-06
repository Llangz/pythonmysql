from mysql.connector import connect


db = connect(host= 'localhost', user='root', passwd= '', database= 'python_db')

cursor = db.cursor()

# sql = "update students set height=5, names = 'John Doe', gender = 'male' where id=1"
sql = "update students set email = 'hfjfkf@yahoo.com'  where id=4"

cursor.execute(sql)

db.commit()

