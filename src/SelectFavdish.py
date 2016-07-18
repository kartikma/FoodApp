import Connection

__author__ = 'vivekmalik'


def getDisharr(dish):
    arr=[]
    arr = dish.split(",")
    print arr
    return arr


def fav7Dish(userid):
    disharr =[]
    sql ="select dish from bucket where userid='%d'"%(userid)
    cursor = Connection.GetConnection()
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        dish = row[0]

    disharr = getDisharr(dish)
    len = disharr.__len__()
    print len
    if(len<7):
        print "please enter 7 dish"
    else:
        i=0
        while(i<7):
            print disharr[i]
            i=i+1




fav7Dish(1)