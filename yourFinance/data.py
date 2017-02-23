#! python3
import os
import shelve
import logging

from yourFinance import user

logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)


class Data:
    FILENAME = 'yourFinance1_3'
    def __init__(self):
        if self.FILENAME + '.dat' not in os.listdir():
            logging.debug('No data file, creating.')
            shelveFile = shelve.open(self.FILENAME)
            shelveFile['users'] = {}
            shelveFile.close()

    def save_user(self, userObj):
        assert isinstance(userObj, user.User), \
            'Wrong argument type (should be User object).'
        shelveFile = shelve.open(self.FILENAME)
        #Shelve does not tracks changes to mutable objects in it so
        #I have to fetch it, change it and write it back.
        fetchFile = shelveFile['users']
        fetchFile[userObj.name + userObj.password] = userObj
        shelveFile['users'] = fetchFile
        shelveFile.close()

    def load_user(self, name, password):
        try:
            shelveFile = shelve.open(self.FILENAME)
            userObj = shelveFile['users'][str(name) + str(password)]
            return userObj
        except:
            raise Exception('No such object in data file.')
        finally:
            shelveFile.close()

    def _remove_user(self, name, password):
        userObj = self.load_user(name, password)
        shelveFile = shelve.open(self.FILENAME)
        fetchFile = shelveFile['users']
        del fetchFile[userObj.name + userObj.password]
        shelveFile['users'] = fetchFile
        shelveFile.close()

    def _show_users(self):
         shelveFile = shelve.open(self.FILENAME)
         print(shelveFile['users'])
         shelveFile.close()