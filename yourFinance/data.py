#! python3
# data.py - stores Data class. Contains functions to save,load,
#  remove and show users.
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
        """Saves user object to shelve file."""
        assert isinstance(userObj, user.User), \
            'Wrong argument type (should be User object).'
        shelveFile = shelve.open(self.FILENAME)
        #Shelve does not tracks changes to mutable objects in it so
        #I have to fetch it, change it and write it back.
        fetchFile = shelveFile['users']
        fetchFile[userObj.name + userObj.password] = userObj
        shelveFile['users'] = fetchFile
        shelveFile.close()
        logging.debug('Data class: User saved.')

    def load_user(self, name, password):
        """Loads user object from shelve file."""
        try:
            shelveFile = shelve.open(self.FILENAME)
            userObj = shelveFile['users'][str(name) + str(password)]
            logging.debug('Data class: User loaded.')
            return userObj
        except:
            raise Exception('No such object in data file.')
        finally:
            shelveFile.close()

    def _remove_user(self, name, password):
        """Removes user object from shelve file."""
        userObj = self.load_user(name, password)
        shelveFile = shelve.open(self.FILENAME)
        fetchFile = shelveFile['users']
        del fetchFile[userObj.name + userObj.password]
        shelveFile['users'] = fetchFile
        shelveFile.close()
        logging.debug('Data class: User removed.')

    def _show_users(self):
        """Prints all users in shelve file. Function helps with testing."""
        shelveFile = shelve.open(self.FILENAME)
        print(shelveFile['users'])
        shelveFile.close()