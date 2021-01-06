# Create Database using Python 

import pymysql
from mysql.connector import cursor

# connect to MySQL
db = pymysql.connect(
    host="localhost", 
    user = "root", 
    password = "Root"
    )


cursor = db.cursor() 
cursor.execute("DROP DATABASE IF EXISTS davedvds"); 
cursor.execute("CREATE DATABASE davedvds"); 
cursor.execute("USE davedvds"); 


cursor.execute("CREATE TABLE dvds(\
    serialNum int NOT NULL AUTO_INCREMENT,\
    title varchar(250),\
    director varchar(250),\
    price int,\
    PRIMARY KEY(serialNum)\
    )"); 

cursor.execute("CREATE TABLE customer(\
    serialNum int NOT NULL AUTO_INCREMENT,\
    title varchar(250),\
    name varchar(250),\
    price int,\
    PRIMARY KEY(serialNum)\
    )"); 

sql1= ("insert into dvds (title, director, price) values ('A Quiet Place', 'John Krasinski', 8.00)")

sql2= ("insert into dvds (title, director, price) values ('The Hangover', 'Todd Phillips', 7.00)")

sql3= ("insert into customer (title, name, price) values ('The Patriot', 'John Smith', 6.00)")

sql4= ("insert into customer (title, name, price) values ('The Hangover', 'Sue Volany', 7.00)")

cursor.execute(sql1)
cursor.execute(sql2)
cursor.execute(sql3)
cursor.execute(sql4)
db.commit()