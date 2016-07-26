from datetime import time, datetime
import user
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.context_processors import csrf
from requests import auth
from rest_framework import status
from Files import addbucket

from FoodAssitant import foodhistory, Foodprefrence, Foodmenu, bucket

from FoodAssitant.serilalizers import food

def login(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'login.html', c)

def register(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'registration.html', c)

def successregister(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'registrationform.html', c)


def create_user(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    email = request.POST.get('email','')
    print username +""+password+""+email
    user = User.objects.create_user(username = username ,password = password ,email = email)
    user.save()
    return HttpResponseRedirect('success/register')


def reset_password():
    test=User.objects.get(username="kartik")
    test.set_password('malik@123')
    test.save()



def user_auth(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    print username+""+password
    user1 = User.objects.filter(username = username ,password = password)
    print user1
    user = authenticate(username = username, password = password)
    print user

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')



def add_food(request):
    a = Foodmenu(foodname =' Egg curry' ,fooddetail ='egg cook with capsicum and onion' , foodprice =300, foodtype ='nonveg')

    a.save()
    test = Foodmenu.objects.all()
    serializer = food (test , many = True)
    if test is not None:
        return HttpResponse(serializer.data,status=status.HTTP_200_OK)
    else:
        return HttpResponse(status = status.HTTP_400_BAD_REQUEST)


def food_history(request):

    f = foodhistory(userid =1 ,foodid =1 ,quantity =1 ,totalprice =250 )
    f.save()
    return HttpResponse(status=status.HTTP_200_OK)


def food_prefrence(request):
    p = Foodprefrence(userid = 1,day ='Saturday' ,foodtype ='nonveg')
    p.save()
    return HttpResponse(status=status.HTTP_200_OK)



def add_bucket(request):
    id =1
    dish =['paneer butter masala','kadhai paneer','palak paneer','paneer tikka','chicken tikka',' butter chicken',' kadhai chicken',' Egg curry']
    user = bucket.objects.filter(userid =id)
    print user
    if not user:
        food =addbucket.generate_dish(dish)
        b = bucket(userid =1,foodbucket =food)
        b.save()
        return  HttpResponse(status =status.HTTP_200_OK)
    else:
        bucket_ar=[]
        food_bucket =addbucket.generate_dish(dish)
        bucket_ar = addbucket.bucket_arr(id)
        #print bucket_arr
        #print food_bucket.__len__()
        count = bucket_ar.__len__()+dish.__len__()

        if count>30:
            print ("no size")
            return  HttpResponse(status =status.HTTP_200_OK)

        else:
            food = addbucket.generate_dish(bucket_ar)+food_bucket
            b = bucket.objects.filter(userid=id).update(foodbucket =food)
      #      b.save()
            return  HttpResponse(status =status.HTTP_200_OK)



class addfood:
     def post(self, request, format=None):
        serializer = food(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serializer.data, status=status.HTTP_201_CREATED)
        return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




