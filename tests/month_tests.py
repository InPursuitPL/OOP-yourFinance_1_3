from nose.tools import *
from yourFinance import month
from yourFinance import stash

def test_init():
    obj = month.Month('jan')
    assert_equal(obj.name, 'jan')

    assert_raises(Exception, month.Month, 'January')

def test_add_stash():
    obj = month.Month('jan')
    stashObj = stash.Stash('wallet', 150)
    obj.add_stash(stashObj)
    assert_equal(len(obj.stashList), 1)
 
