import datetime
from FoodAssitant import Foodprefrence

__author__ = 'vivekmalik'

def get_prefrence(userid):
    day = datetime.datetime.now()
    today = day.strftime("%A")
    food_type = Foodprefrence.objects.get(day =today ,userid =1)
    return  food_type.foodtype
    print food_type.foodtype



get_prefrence(1)