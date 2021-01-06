# David Markham
# 19-11-2020
# Here we put all the previous snippets of code in one program using a D.A.O, which is a Data Access Object.
# Data Access Object Pattern or DAO pattern is used to separate low level data accessing API or operations from high level business services.
# It is an application program interface (API) available with Microsoft's Visual Basic,
# that lets a programmer request access to a Microsoft Access database.

import mysql.connector
from mysql.connector import cursor
#import mydbconfig as cfg 

# Make database connection
class DvdDao:
    db = "" # Variable
    def __init__(self): # Create function 
        self.db = mysql.connector.connect(
            host = 'localhost',
            user= 'root',
            password = 'Root',
            database ='dvds'
        )
        #print ("connection made")

    def create(self, dvd): # CREATE function.
        cursor = self.db.cursor()
        sql = "insert into dvds (serialNum, title, director, price) values (%s,%s,%s,%s)"
        values = [ # Values passed into function. 
            dvd['serialNum'],
            dvd['title'],
            dvd['director'],
            dvd['price']  
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def getAll(self): # GETALL function 
        cursor = self.db.cursor()
        sql = 'select * from dvds'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)

        return returnArray

    def findById(self, serialNum): # Find all where ISBN = values.
        cursor = self.db.cursor()
        sql = 'select * from dvds where serialNum = %s'
        values = [ serialNum ] 
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)
        

    def update(self, dvd): # UPDATE dvd
       cursor = self.db.cursor()
       sql = "update dvds set title = %s, director = %s, price = %s where serialNum = %s"
       values = [
           dvd['title'],
           dvd['director'],
           dvd['price'],
           dvd['serialNum'] 

       ]
       cursor.execute(sql, values)
       self.db.commit()
       return dvd

    def delete(self, serialNum): # Delete dvd
       cursor = self.db.cursor()
       sql = 'delete from dvds where serialNum = %s'
       values = [serialNum]
       cursor.execute(sql, values)
       
       return {}



    def convertToDict(self, result):
        colnames = ['serialNum','title', 'director', 'price']
        dvd = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                dvd[colName] = value
        return dvd

dvdDao = DvdDao() 