import Connection

__author__ = 'vivekmalik'


def GetFoodList():
    cursor = Connection.GetConnection()
    sql ="select * from fooditems"
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
       # foodid = row[0]
        foodname = row[0]
        fooddetail = row[1]
        price=row[3]

        print("foodname = %s , detail =%s , Price = %d ")%(foodname,fooddetail,price)


GetFoodList()