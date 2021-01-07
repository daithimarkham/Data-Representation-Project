# David Markham
# 19-11-2020
# Here we put all the previous snippets of code in one program using a D.A.O, which is a Data Access Object.
# Data Access Object Pattern or DAO pattern is used to separate low level data accessing API or operations from high level business services.
# It is an application program interface (API) available with Microsoft's Visual Basic,
# that lets a programmer request access to a Microsoft Access database.



import mysql.connector
from mysql.connector import cursor
import dbconfig as cfg 



class DvdDAO:
    db=""
    def __init__(self): 
        self.db = mysql.connector.connect(
        host =       cfg.mysql['host'],
        user =       cfg.mysql['user'],
        password =   cfg.mysql['password'],
        database =   cfg.mysql['database']
        )
    
            
    def create(self, values):
        cursor = self.db.cursor()
        sql = "insert into dvds (title, director, price) values (%s,%s,%s)" 
        cursor.execute(sql, values)

        self.db.commit()
        return cursor.lastrowid 

    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from dvds"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result)) 

        return returnArray

    def findByID(self, id):
        cursor = self.db.cursor()
        sql="select * from dvds where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDictionary(result) 

    def update(self, values):
        cursor = self.db.cursor()
        sql="update dvds set title = %s, director = %s, price = %s  where id = %s"
        cursor.execute(sql, values)
        self.db.commit()

    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from dvds where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.db.commit()
        print("delete done")

    def convertToDictionary(self, result):
        colnames=['id','Title','Director', "Price"]
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item
        
DvdDao = DvdDAO() 