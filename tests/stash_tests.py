from nose.tools import *
from yourFinance.stash import Stash

def test_init():
    obj = Stash('wallet', 120.556789)
    assert_equal(obj.name, 'wallet')
    assert_equal(obj.amount, 120.56)

    assert_raises(Exception, Stash, 'wallet', 'a lot')

def test_increase_and_decrease():
    obj = Stash('wallet', 120.556789)
    obj.increase_amount(3.45678)
    assert_equal(obj.amount, 124.02)
    obj.decrease_amount(22.123)
    assert_equal(obj.amount, 101.9)
 
