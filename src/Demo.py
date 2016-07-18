import Connection
import MySQLdb

__author__ = 'vivekmalik'

def  Getuserid():
    sql = "select userid from login where username ='%s'" %('vivek')
    cursor = Connection.GetConnection()
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        userid = row[0]

    print (userid)
    return userid

