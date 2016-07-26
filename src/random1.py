import random
from Files import addbucket

from FoodAssitant import Foodmenu, foodhistory

__author__ = 'vivekmalik'

def random_dish_generator(userid):
    bucket =[]
    bucket = addbucket.bucket_arr(userid)
    n = bucket.__len__();
    n = Foodmenu.objects.count()
    r = int(random.random()* n)+1
    return bucket[r]


#random_dish_generator(1)