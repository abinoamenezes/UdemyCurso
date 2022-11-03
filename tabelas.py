import mysql.connector

mydb2=mysql.connector.connect(
    host='localhost',
    user='abino1',
    password='abino',
    database='mydatabas'
)
print(mydb2)

mycursor=mydb2.cursor()
sql=""" INSERT INTO produtos (id,nome)
    VALUES( %s,%s)
    """
val=[('169','Camisinha'),
    ('151','Pistola'),
    ('188','Cerveja')
]
mycursor.executemany(sql,val)
mydb2.commit()
