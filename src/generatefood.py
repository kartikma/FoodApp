
from django.db import connection
from Files import getfoodhistory,random1,getfoodprefrence

from FoodAssitant import foodhistory, Foodmenu

__author__ = 'vivekmalik'


def today_food(userid):
    lastorder =[]
    todayfood = random1.random_dish_generator(userid)
    #print todayfood
    lastorder =getfoodhistory.food_history(userid)
    if todayfood in lastorder:
        today_food(userid)

    return todayfood




def generate_food(userid):
    food = today_food(userid)
    #print food
    day_food_type = getfoodprefrence.get_prefrence(userid)
    #print day_food_type
    food_type = Foodmenu.objects.get(foodname = food)
    #print food_type.foodtype
    food1 = food_type.foodtype
    #print (food1 == day_food_type)
    if(food1 == day_food_type):
        print food
    else:
        generate_food(userid)


generate_food(1)
