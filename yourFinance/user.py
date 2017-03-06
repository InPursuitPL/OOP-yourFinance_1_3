#! python3
# user.py - stores User class, which holds year objects in dictionary.

from yourFinance import year


class User:
    def __init__(self, name='', password=''):
        self.yearDict = {}
        # There are some default values that can be changed by the program.
        # No (g/s)etter as these name may be anything.I will access it
        # directly.
        self.stashNames = ['bank account', 'savings', 'wallet', 'others']
        self.currentCosts = ['rent and other charges', 'transportation',
                             'clothes', 'food',
                             'hobby', 'others']
        self.mothlyCosts = {
                'existence amount': 1500,
                    'minimal amount': 2000,
                    'standard amount': 3000,
                }

        if name == '':
            self.set_name()
        else:
            self.name = str(name)

        if password == '':
            self.set_password()
        else:
            self.password = str(password)

    def set_name(self):
        """Sets user name if it was not given while being created."""
        name = input('User name: ')
        self.name = name

    def set_password(self):
        """Sets user password if it was not given while being created."""
        password = input('User password: ')
        self.password = str(password)

    def add_year(self, yearObj):
        """Adds year to dictionary. Replaces if already there."""
        assert isinstance(yearObj, year.Year),\
            'Wrong argument type (should be Year object).'
        self.yearDict[yearObj.number] = yearObj

    def remove_year(self, yearObj):
        """Removes year from dictionary. Error if not present."""
        assert isinstance(yearObj, year.Year),\
            'Wrong argument type (should be Year object).'
        # Function will raise error if year obj with this name is not in dict.
        try:
            del self.yearDict[yearObj.number]
        except KeyError:
            raise Exception('No object with this name in years dictionary.')

    def show_funds(self):
        """Returns string with years info."""
        fundsString = '\n'
        for year in sorted(self.yearDict.keys()):
            fundsString += self.yearDict[year].show_year()
        return fundsString
