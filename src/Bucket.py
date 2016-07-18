import RandomGenerator
import Select

__author__ = 'vivekmalik'

import MySQLdb

db = MySQLdb.connect("localhost","root","root","foodapp" )
cursor = db.cursor()


def  Auto_genrator(list =[]):
    dishname = RandomGenerator.Random_generator()
    while dishname in list:
        dishname = RandomGenerator.Random_generator()


    #print(dishname)
    return dishname






def  Getuserid(name):
    sql = "select userid from login where username ='%s'" %(name)
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        userid = row[0]

    #print (userid)
    return userid

dish =[]

#id = Getuserid();
#dish=Select.SelectOrder(id)
#Auto_genrator(dish)
#Getuserid()
