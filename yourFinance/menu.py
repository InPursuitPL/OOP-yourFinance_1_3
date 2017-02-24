#! python3

import sys
from yourFinance import data, user, year, month, stash

class Menu:
    '''Shows options of the program.'''
    def __init__(self, userObj):
        self.userObj = userObj
        self.choices = {
            "1": self.add_month,
            "2": self.choose_time_to_display,
            "3": self.run_analyze_menu,
            "4": self.configure_settings,
            "5": self.exit,
        }
        self.run()

    def display_menu(self):
        '''Displays menu options.'''
        print('''\nWelcome in yourFinance program. What would you like to do:
1. Add new data for the month.
2. Check data for the whole time, year or month.
3. Analyze data.
4. Configure settings.
5. Exit.
''')

    def run(self):
        '''User can decide here which option to choose.'''
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice.".format(choice))

    def add_month(self):
        '''Lets user to input and save data for certain month.'''
        yearObj = year.Year()
        if yearObj.number in self.userObj.yearDict:
            yearObj = self.userObj.yearDict[yearObj.number]
        monthObj = month.Month()
        if monthObj.name in yearObj.monthDict:
            print('This month was already planned.')
            answer = input('You want to do it again? (y/n)')
            if answer.lower().startswith('n'):
                return None
        if self.userObj.stashNames == []:
            print('Please configure your money deposition places before proceeding')
            self.configure_stashes_names()
        for stashName in self.userObj.stashNames:
            print('Name of money deposition place: {}'.format(stashName))
            stashObj = stash.Stash(stashName)
            monthObj.add_stash(stashObj)
        yearObj.add_month(monthObj)
        self.userObj.add_year(yearObj)
        data.Data().save_user(self.userObj)
        print('Data for year {} saved:'.format(yearObj.number))
        print(monthObj.show_month())
        input('\nHit enter to go back to menu.')

    def choose_time_to_display(self):
        '''User can decide which part of data he wants to display.'''
        pass

    def run_analyze_menu(self):
        '''Runs submenu with more options.'''
        pass

    def configure_settings(self):
        '''Gives options of settings to configure and save.'''
        pass

    def configure_stashes_names(self):
        userObj.stashNames = ['account', 'wallet', 'others']

    def exit(self):
        sys.exit()


if __name__ == '__main__':
    userObj = user.User('Lucas', 1234)
    Menu(userObj)