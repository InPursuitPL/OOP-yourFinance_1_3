#! python3

from yourFinance import year

class User:
    def __init__(self, name='', password=''):
        self.yearDict = {}
        #No (g/s)etter as stash name may be anything. It is Python so
        #I will access it directly.
        self.stashNames = []
        if name == '':
            self.set_name()
        else:
            self.name = str(name)

        if password == '':
            self.set_password()
        else:
            self.password = str(password)

    def set_name(self):
        name = input('User name: ')
        self.name = name

    def set_password(self):
        password = input('User password: ')
        self.password = str(password)

    def add_year(self, yearObj):
        assert isinstance(yearObj, year.Year),\
            'Wrong argument type (should be Year object).'
        self.yearDict[yearObj.number] = yearObj

    def remove_year(self, yearObj):
        assert isinstance(yearObj, year.Year),\
            'Wrong argument type (should be Year object).'
        # Function will raise error if year obj with this name is not in dict.
        try:
            del self.yearDict[yearObj.number]
        except:
            raise Exception('No object with this name in years dictionary.')

    def show_funds(self):
        fundsString = '\n'
        for year in sorted(self.yearDict.keys()):
            fundsString += self.yearDict[year].show_year()

        return fundsString
