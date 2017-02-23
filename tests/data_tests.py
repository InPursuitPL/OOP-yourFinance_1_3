import os
from nose.tools import *
from yourFinance import data, user, year, month

def create_user_obj():
   yearObj = year.Year(2017)
   monthObj = month.Month('jan')
   month2Obj = month.Month('feb')
   yearObj.add_month(monthObj)
   yearObj.add_month(month2Obj)
   obj = user.User('Lucas', 'randomPassword')
   obj.add_year(yearObj)
   year2Obj = year.Year(2018)
   year2Obj.add_month(month2Obj)
   obj.add_year(year2Obj)
   return obj

def test_init():
   obj = data.Data()
   assert_equal(obj.FILENAME + '.dat' in os.listdir(), True)


def test_save_load_remove_user():
   obj = data.Data()
   userObj = user.User('Testguy', 1234)
   obj.save_user(userObj)
   assert_equal(obj.load_user('Testguy', '1234').name, 'Testguy')
   obj._remove_user('Testguy', '1234')
   assert_raises(Exception, obj.load_user, 'Testguy', '1234')
    



   
