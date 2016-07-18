import MySQLdb
import Connection

__author__ = 'vivekmalik'
db = MySQLdb.connect("localhost","root","root","foodapp" )

def UserIsExist(username):
    cursor = Connection.GetConnection()
    sql ="select username from login where username='%s' " %(username)
    cursor.execute(sql)
    res = cursor.fetchall()
    for row in res:
        return row[0]


def Register(name,password):
    cursor = Connection.GetConnection()
    sql ="Insert into login(username,password) values('%s','%s') "%(name,password)
    print sql
    cursor.execute(sql)
    user = UserIsExist(name)
    if user is None:
        cursor.execute('''Insert into login(username,password) values(%s,%s)''',(name,password))
        db.commit()
        print("user created")
    else:
        print("user is exist")

    db.close()

Register('mohit','malik')
