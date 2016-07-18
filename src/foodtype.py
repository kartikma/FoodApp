import Connection
import datetime

__author__ = 'vivekmalik'

def GetFoodType(userid):
    day = datetime.datetime.now()
    today = day.strftime("%A")
    cursor =Connection.GetConnection()
    sql="select foodtype from foodprefrence where userid='%d' and day='%s'" %(userid,today)
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        food_type= row[0]

    #print food_type
    return food_type

def GetDishType(foodid):
    cursor = Connection.GetConnection()
    sql = "select foodtype from fooditem where foodid ='%d'" %(foodid)
    cursor.execute(sql)
    result =cursor.fetchall()
    for row in result:
        dishtype = row[0]

    #print dishtype
    return dishtype


GetFoodType(1)
GetDishType(1)