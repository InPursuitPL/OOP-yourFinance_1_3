#! python3

from yourFinance import month

class Year:
    def __init__(self, number=''):
        #Months in dict with month name as key - it will be easier to search
        #for a certain month without the need to iterate through all elements
        #as it woud be if we would have list instead of a dict.
        self.monthDict = {}
        if number == '':
            self.set_number()
        else:
            assert isinstance(number,int), "Wrong data type of year number."
            self.number = number

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
        #Function will replace data for the given key, that is already in dict.
        #Values will be month names, as it will be easier to find certain month
        #object. 
        self.monthDict[monthObj.name] = monthObj

    def remove_month(self, monthObj):
        assert isinstance(monthObj,month.Month), 'Wrong argument type (should be Month object).'
        #Function will raise error if month obj with this name is not in dict.
        try:
            del self.monthDict[monthObj.name]
        except:
            raise Exception('No object with this name in months dictionary.')

    def show_year(self):
        yearString = str(self.number) + '\n\n'
        for monthName in month.Month.MONTHS_NAMES:
            if monthName in self.monthDict.keys():
                yearString += self.monthDict[monthName].show_month()

        return yearString
