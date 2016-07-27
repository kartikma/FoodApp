from django.db import connection
from FoodAssitant import foodhistory, Foodmenu

__author__ = 'vivekmalik'

def food_history(userid):
    data =[]
    food =[]
    cursor = connection.cursor()
    sql ="select * from FoodAssitant_foodhistory where userid='%d' order BY  orderdate DESC limit 3"%(userid)
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        i = row[2]
        data.append(i)

    for i in data:
        f = Foodmenu.objects.get(foodid = i)
        #print f.foodname
        food.append((f.foodname).encode("utf-8"))
    return food

print food_history(1)