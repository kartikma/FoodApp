import Connection

__author__ = 'vivekmalik'
import MySQLdb
db = MySQLdb.connect("localhost","root","root","foodapp" )

def deleteBucket(id):
    sql="delete from Bucket where userid=%d"%(id)
    print sql
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()



deleteBucket(1)