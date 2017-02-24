#! python3

from yourFinance import stash

class Month:
    MONTHS_NAMES = ['jan', 'feb', 'mar', 'apr', 'may', 'jun',
                    'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    def __init__(self, name=''):
        #This totalStash will automatically aggregate all amounts from other
        #stashes that will be placed in stashList.
        self.totalStash = stash.Stash('Total', 0)
        self.stashList = []
        if name == '':
            self.set_name()
        else:
            assert name in Month.MONTHS_NAMES, 'Wrong month name delivered to <name> variable.'
            self.name = name
            
    def set_name(self):
        while True:
            name = input('Name of the month (as 3 letter abbreviation): ')
            if name[:3].lower() not in Month.MONTHS_NAMES:
                print('It is not a proper name for month.')
                continue
            name = name[:3].lower()
            break
        self.name = name

    def add_stash(self, stashObj):
        assert isinstance(stashObj, stash.Stash), 'Wrong argument type (should be Stash object).'
        #Function adds Stash objects to the stashList but does it "by name"
        #which means, that it is not possible to add two objects (even with
        #different amounts) with the same object's name. This is because of
        #two reasons:
        #1) prevents confusion from the user perspective
        #2) helps to handle objects after saving/loading (as long as data
        #   are handled in file system) when object become alike but is not
        #   the same as before saving/loading, in the terms of location.
        for obj in self.stashList:
            assert stashObj.name != obj.name, 'Stash object with this name already in list.'
        self.stashList.append(stashObj)
        #Adds amount to totalStash.amount as I want this one to be
        #automatically updated.
        self.totalStash.amount += stashObj.amount

    def remove_stash(self, stashObj):
        assert isinstance(stashObj, stash.Stash), 'Wrong argument type (should be Stash object).'
        #Function removes Stash objects from the stashList but does it "by name"
        #of the stashes. Please have a look at upper comment lines in add_stash
        # function to check why I use adding/removing by name of the objects.
        nothingRemoved = True
        for obj in self.stashList:
            if stashObj.name == obj.name:
                self.stashList.remove(obj)
                nothingRemoved = False
                break
        if nothingRemoved:
            raise Exception('No object with this name in objects list.')
        #Subtracts amount from totalStash.amount as I want this one to be
        #automatically updated.
        self.totalStash.amount -= stashObj.amount

    def show_month(self):
        monthString = self.name + '\n' + self.totalStash.show_stash() + '\n'
        for stash in self.stashList:
            monthString += stash.show_stash() + '\n'
        monthString += '\n'

        return monthString
