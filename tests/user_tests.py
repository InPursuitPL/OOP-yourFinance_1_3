from nose.tools import *
from yourFinance import user, year, month, stash

answer ='''
2017

jan
Total: 0.0

feb
Total: 0.0

2018

feb
Total: 0.0

'''

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
   obj = user.User('Lucas', 12345)
   assert_equal(obj.name, 'Lucas')
   assert_equal(obj.password, '12345')

def test_add_remove_year():
   obj = create_user_obj()
   assert_equal(len(obj.yearDict), 2)
   assert_equal(obj.yearDict[2017].number, 2017)
   assert_equal(len(obj.yearDict[2017].monthDict), 2)
   yearObj = year.Year(2018)
   obj.remove_year(yearObj)
   assert_equal(len(obj.yearDict), 1)
   assert_raises(Exception, obj.remove_year, 2017)
    
def test_show_funds():
   obj = create_user_obj()
   assert_equal(obj.show_funds(), answer)

   
