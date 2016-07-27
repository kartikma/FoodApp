from django.db import models

__author__ = 'vivekmalik'

class MyModel(models.Model):

    class Meta:
        managed = True      # add this
        app_label = 'FoodAssitant'


class Login(models.Model):
    userid =models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password =models.CharField(max_length=25)
    #last_name = models.CharField(max_length=25)


class Foodmenu(models.Model):
    foodid = models.AutoField(primary_key = True)
    foodname = models.CharField(max_length=30)
    fooddetail = models.CharField(max_length=300)
    foodprice = models.IntegerField()
    foodtype = models.CharField(max_length= 20)



class foodhistory(models.Model):
    userid = models.IntegerField()
    foodid = models.IntegerField()
    quantity = models.IntegerField()
    totalprice = models.IntegerField()
    orderdate =models.DateField(auto_now=True)


class bucket(models.Model):
    userid = models.IntegerField()
    foodbucket = models.CharField(max_length=300)


class Foodprefrence(models.Model):
    userid = models.IntegerField()
    day =models.CharField(max_length=50)
    foodtype = models.CharField(max_length=20)



