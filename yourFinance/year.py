#! python3

import month

class Year:
    def __init__(self, number=''):
        self.monthDict = {}
        if number == '':
            self.set_number()
        else:
            assert isinstance(number,int), "Wrong data type of year number."

    def set_number(self):
        while True:
            number = input('Number of this year: ')
            try:
                self.number = int(number)
                break
            except:
                print('It is not a proper number for year.')
                continue

    def add_month(self, monthObj):
        assert isinstance(monthObj,month.Month), 'Wrong argument type (should be Month object).'
        self.monthDict[monthObj.name] = monthObj

    def remove_month(self, monthObj):
        pass