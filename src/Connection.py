__author__ = 'vivekmalik'
import MySQLdb
#@staticmethod
def GetConnection():
      db = MySQLdb.connect("localhost","root","root","foodapp" )
      cursor = db.cursor()
      return cursor
