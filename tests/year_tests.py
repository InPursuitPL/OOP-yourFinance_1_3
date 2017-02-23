from nose.tools import *
from yourFinance import year, month, stash

answer = '''2017

jan
Total: 350.0
wallet: 150.0
bank: 200.0

feb
Total: 550.0
wallet: 100.0
bank: 450.0

'''

def test_init():
   obj = year.Year(2017)
   assert_equal(obj.number, 2017)

   assert_raises(Exception, year.Year, '2k17')

def test_add_remove_month():
    obj = year.Year(2017)
    monthObj = month.Month('jan')
    obj.add_month(monthObj)
    assert_equal(len(obj.monthDict), 1)

    assert_equal(obj.monthDict['jan'].name, 'jan')
    assert_equal(len(obj.monthDict['jan'].stashList), 0)

    month2Obj = month.Month('jan')
    stashObj = stash.Stash('wallet', 150)
    month2Obj.add_stash(stashObj)
    obj.add_month(month2Obj)
    assert_equal(len(obj.monthDict), 1)
    assert_equal(obj.monthDict['jan'].name, 'jan')
    assert_equal(len(obj.monthDict['jan'].stashList), 1)

    obj.remove_month(month2Obj)
    assert_equal(len(obj.monthDict), 0)
    assert_raises(Exception, obj.remove_month, monthObj)
    
def test_show_year():
   obj = year.Year(2017)
   monthObj = month.Month('jan')
   stashObj = stash.Stash('wallet', 150)
   stash2Obj = stash.Stash('bank', 200)
   monthObj.add_stash(stashObj)
   monthObj.add_stash(stash2Obj)
   month2Obj = month.Month('feb')
   stash3Obj = stash.Stash('wallet', 100)
   stash4Obj = stash.Stash('bank', 450)
   month2Obj.add_stash(stash3Obj)
   month2Obj.add_stash(stash4Obj)
   obj.add_month(monthObj)
   obj.add_month(month2Obj)
   assert_equal(obj.show_year(), answer)
   
