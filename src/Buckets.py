import Connection
import SelectFavdish

__author__ = 'vivekmalik'

import MySQLdb

db = MySQLdb.connect("localhost","root","root","foodapp" )



def FavDish(dish=[]):
    #len = SelectFavdish.getDisharr(dish).__len__()
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


def Insert(Id,dish=[]):
    fav_dish=FavDish(dish)

    cursor =db.cursor()
    sql = "insert into bucket VALUES('%d','%s')" % \
    (Id,fav_dish)

    print(sql)
    cursor.execute(sql)
    db.commit()




dish =['palak','paneer','chicken','bhindi','aloo','tikka','Rice']
#print(dish.__len__())
print FavDish(dish)
Insert(3,dish)

