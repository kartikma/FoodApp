__author__ = 'vivekmalik'

import MySQLdb
import time
db = MySQLdb.connect("localhost","root","root","foodapp" )


def orderList(userid,orderdate,totalprice):
    sql = "insert into orderlist VALUES ('%d','%s','%d')"%(userid,orderdate,totalprice)
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()


date = time.strftime("%Y-%m-%d")
print date
orderList(1,date,550)

