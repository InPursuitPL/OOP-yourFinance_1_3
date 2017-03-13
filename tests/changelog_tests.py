import os
from nose.tools import *
from yourFinance import data, user, year, month, changelog

os.chdir('.\\tests')


def create_user_obj():
   yearObj = year.Year(2017)
   monthObj = month.Month('jan')
   month2Obj = month.Month('feb')
   yearObj.add_month(monthObj)
   yearObj.add_month(month2Obj)
   obj = user.User('ChangelogTester', 'randomPassword')
   obj.add_year(yearObj)
   year2Obj = year.Year(2018)
   year2Obj.add_month(month2Obj)
   obj.add_year(year2Obj)
   return obj

def test_update_and_save_change():
   # Removing previous changelog file if exists.
   FILENAME = data.Data.FILENAME
   changelogFileName = '{}{}.txt'.format(FILENAME, '_changelog')
   if changelogFileName in os.listdir():
      os.unlink(changelogFileName)

   obj = create_user_obj()
   changelog.Changelog().update(obj)

   changelogFileText = open(changelogFileName).read()
   
   assert_equal(True, '#####USER: ChangelogTester' in changelogFileText)

   os.unlink(changelogFileName)


   
