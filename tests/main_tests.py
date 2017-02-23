from nose.tools import *
from yourFinance import data, user
from main import return_user_obj_or_None

def test_return_user_obj_or_None():
   assert_equal(return_user_obj_or_None('NotExistingGuy', 1234, False), None)
   data.Data().save_user(user.User('GuyForMainTest', 1234))
   returnValue = return_user_obj_or_None('GuyForMainTest', 1234, False)
   #I have used try/finally because I want to be absolutely sure that, even if
   #test would fail, user will still be removed from database to not to cause
   #further problems.
   try:
      assert_equal(returnValue.password, '1234')
   except:
      raise Exception('Test of main file has failed.')
   finally:
      data.Data()._remove_user(returnValue.name, returnValue.password)
   #Same here.
   try:
      assert_equal(return_user_obj_or_None('NowCreatedGuy',
                                           'banana',
                                           True).password,
                   'banana')
   except:
      raise Exception('Test of main file has failed.')
   finally:
      data.Data()._remove_user('NowCreatedGuy','banana')

   
