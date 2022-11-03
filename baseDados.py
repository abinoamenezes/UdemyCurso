from platform import mac_ver
from sqlite3 import sqlite_version
import mysql.connector

mydb= mysql.connector.connect(
    host='localhost',
    user='abino1',
    password='abino',
    database='mydatabas'

)
mycursor=mydb.cursor()
sql="""SELECT usuarios.nome AS nome,
produtos.nome AS favorito
FROM usuarios RIGHT JOIN produtos ON usuarios.fav=produtos.id"""
mycursor.execute(sql)
myRsult=mycursor.fetchall()
for x in myRsult:
    print(x)



