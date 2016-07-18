__author__ = 'vivekmalik'
import MySQLdb

db = MySQLdb.connect("localhost","root","root","foodapp" )

cursor = db.cursor()

#sql = "insert into city VALUES(null, 'Mars City', 'MAC', 'MARC', 1233)"
name = "Some new city"
country_code = 'PSE'
district = 'Someyork'
population = 10008

sql = "insert into city VALUES('%s', '%s', '%s', %d)" % \
 (name, country_code , district, population)
cursor.execute(sql)
db.commit()   # you need to call commit() method to save
              # your changes to the database


db.close()