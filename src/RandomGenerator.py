import Connection

__author__ = 'vivekmalik'

def Random_generator():
    sql ="SELECT foodid FROM fooditems  ORDER BY RAND() LIMIT 1 "
    #print(sql)
    cursor = Connection.GetConnection()
    cursor.execute(sql)
    RandomId=(cursor.fetchall())
    for row in RandomId:
        food_id =row[0]


    #print food_id
    return food_id