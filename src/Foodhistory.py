import Connection

__author__ = 'vivekmalik'


def GetFoodHistory(userid):
    cursor =Connection.GetConnection()
    sql ="select * from foodhistory where userid='%d'"%(userid)
    cursor.execute(sql)
    result = cursor.fetchall()
    if result is None:
        print("no food history")
    else:
        for row in result:
            orderdate=row[1]
            foodid=row[2]
            Quantity=row[3]
            totalprice =row[4]

            print("orderdate =  %s,  foodid =  %d, Quantity= %d , Price  =%d ")%(orderdate,foodid,Quantity,totalprice)





GetFoodHistory(1)