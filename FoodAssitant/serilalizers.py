from rest_framework import serializers
from FoodAssitant.models import Login, Foodmenu

__author__ = 'vivekmalik'

class food(serializers.ModelSerializer):

    class Meta:
        model = Foodmenu
        fields = ('foodid' , 'foodname' ,'fooddetail', 'foodprice', 'foodtype')





