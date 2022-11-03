import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='abino',
    password='abino8986@'
)
my_cursor= mydb.cursor()
#my_cursor.execute('CREATE DATABASE myBase')

my_cursor.execute('SHOW DATABASES')
for x in my_cursor:
    print(x)
