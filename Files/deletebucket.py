from django import db
from django.db import connection

__author__ = 'vivekmalik'


def delete_bucket(userid):
    sql="delete from FoodAssitant_bucket where userid=%d"%(userid)
    cursor = connection.cursor()
    cursor.execute(sql)
    db.commit()
