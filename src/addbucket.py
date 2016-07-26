from django import db
from django.db import connection
from FoodAssitant import bucket

__author__ = 'vivekmalik'

def generate_dish(dish=[]):
    if dish.__len__()<7:
        print("please enter 7 item")

    else:
        s=""
        i=0
        while(i<dish.__len__()):
            s=s+dish[i]+","
            i =i+1
            #print s
        return s



def bucket_arr(userid):
    food_arr=[]
    f = bucket.objects.get(userid =1)
    print f.foodbucket
    food= f.foodbucket
    for i in food.split(',') :
        if not i=='':
            food_arr.append(i.encode("utf-8"))
    return food_arr
    print  food_arr.__len__()











