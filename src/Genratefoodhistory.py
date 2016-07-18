import time

__author__ = 'vivekmalik'
import MySQLdb

db = MySQLdb.connect("localhost","root","root","foodapp" )

def foodHistory(userid,date,foodid,quantity,price):
    sql="insert into foodhistory VALUES ('%d','%s','%d','%d','%d')"%(userid,date,foodid,quantity,price)
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()


date = time.strftime("%Y-%m-%d")

foodHistory(1,date,2,2,500)
