from nose.tools import *
from yourFinance import month, stash
def test_init():
    obj = month.Month('jan')
    assert_equal(obj.name, 'jan')

    assert_raises(Exception, month.Month, 'January')

def test_add_remove_stash():
    obj = month.Month('jan')
    stashObj = stash.Stash('wallet', 150)
    obj.add_stash(stashObj)
    assert_equal(len(obj.stashList), 1)

    stash2Obj = stash.Stash('bank', 200)
    obj.add_stash(stash2Obj)
    assert_equal(len(obj.stashList), 2)
    assert_equal(obj.totalStash.amount, 350)

    stash3Obj = stash.Stash('sock', 50)
    assert_raises(Exception, obj.remove_stash, stash3Obj)

    obj.remove_stash(stash2Obj)
    assert_equal(len(obj.stashList), 1)
    assert_equal(obj.totalStash.amount, 150)

def test_show_month():
    obj = month.Month('jan')
    stashObj = stash.Stash('wallet', 150)
    obj.add_stash(stashObj)
    stash2Obj = stash.Stash('bank', 200)
    obj.add_stash(stash2Obj)
    answer = 'jan\nTotal: 350.0\nwallet: 150.0\nbank: 200.0\n\n'
    assert_equal(obj.show_month(), answer)
