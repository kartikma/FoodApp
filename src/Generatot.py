import Bucket
import Connection
import Select
import foodtype

__author__ = 'vivekmalik'
def GetFoodName(id):
    cursor = Connection.GetConnection();
    sql ="select foodname from fooditem where foodid ='%d'" %(id)
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        foodid = row[0]

    print foodid
    return foodid

def DishGenerator(name):
    id = Bucket.Getuserid(name)
    dish = Select.SelectOrder(id)
    foodid =Bucket.Auto_genrator(dish)
    Food_type = foodtype.GetDishType(foodid)
    Day_food = foodtype.GetFoodType(id)
    if(Food_type == Day_food):
        return foodid
    else:
        DishGenerator(name)




name = raw_input("enter the name")
id = DishGenerator(name)
GetFoodName(id)

