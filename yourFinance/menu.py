#! python3
# menu.py - main menu for yourFinance program. Can be tested as script,
# without logging through main.py module.
import sys
import logging

from yourFinance import changelog, data, user, year, month, stash

logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

# This is for Observer design pattern. I've created it outside Menu class
# because in some places I want to use it before instantiating this class
# (eg. in case this module is running as a script or in main.py) as this
# would also trigger main menu running. Other way is to move __init__
# functionality into different function.
observersList = [data.Data().update, changelog.Changelog().update ]
def notify_observers(userObj):
    """Observer design pattern - notifies observers."""
    for observer in observersList:
        observer(userObj)


class Menu:
    """Shows options of the program."""
    # Leave it as class attribute to let it be inherited.
    display_menu = '''\nWhat would you like to do:
    1. Add new data for the month.
    2. Check data for the whole time, year or month.
    3. Analyze data.
    4. Configure settings.
    5. Exit.
    '''

    def __init__(self, userObj):
        self.userObj = userObj
        mainChoices = {
            "1": self.add_month,
            "2": self.display_time,
            "3": self.run_analyze_menu,
            "4": self.configure_settings,
            "5": self.exit,
        }
        self.run(self.display_menu, mainChoices)

    def run(self, textMenu, choices):
        """User can decide here which option to choose."""
        while True:
            print(textMenu)
            choice = input("\nEnter an option: ")
            action = choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice.".format(choice))
            # To ensure that only main menu will be in loop. Other menus,
            # which are used as different, inheriting classes, should
            # be viewed once and then come back to main menu.
            if textMenu != self.display_menu:
                break

    def add_month(self):
        """Lets user to input and save data for certain month."""
        # User inputs about year number and later about month name,
        # stash names and values are being asked internally, while
        # creating certain objects.
        yearObj = year.Year()
        if yearObj.number in self.userObj.yearDict:
            yearObj = self.userObj.yearDict[yearObj.number]

        monthObj = month.Month()
        # Leaves function if user decided to not to override month.
        if yearObj.add_month(monthObj) == False:
            return
        for stashName in self.userObj.stashNames:
            yearObj.monthDict[monthObj.name].add_stash(stash.Stash(stashName))

        self.userObj.add_year(yearObj)
        notify_observers(self.userObj)

        print('\nData for year {} saved:'.format(yearObj.number))
        print(yearObj.monthDict[monthObj.name].show_month())
        input('\nHit enter to go back to menu.')

    def display_time(self):
        """Displays user stashes data for certain time."""
        year = input('Which year data you want to display? '
                     'Or hit enter to display all data: ')
        if year == '':
            print(self.userObj.show_funds())
        else:
            month = input('Which month you want to display? '
                          'Or hit enter to display whole year data: ')
            if month == '':
                try:
                    print(self.userObj.yearDict[int(year)].show_year())
                except KeyError:
                    print('\nNo data in database for {}'.format(year))
            else:
                try:
                    print(year, self.userObj.yearDict[int(year)].monthDict[month].show_month())
                except KeyError:
                    print('\nNo data in database for {}'.format(month))
                except ValueError:
                    print('\nNo data in database for {}'.format(year))
        input('\nHit enter to go back to menu.')

    def run_analyze_menu(self):
        """Runs submenu with more options."""
        # I need to import it here because of circular dependent
        # imports (imported class uses Menu as superclass). There
        # would be an error if importing it in the beginning.
        from yourFinance import analyze_menu
        analyze_menu.AnalyzeMenu(self.userObj)

    def configure_settings(self):
        """Runs submenu with more options."""
        # I need to import it here because of circular dependent
        # imports (imported class uses Menu as superclass). There
        # would be an error if importing it in the beginning.
        from yourFinance import configure_menu
        configure_menu.ConfigureMenu(self.userObj)
        # I need to load user from file, because configure menu was
        # working on its own object of the same user and saved it at
        # the end.
        self.userObj = data.Data().load_user(
            self.userObj.name,
            self.userObj.password)

    def exit(self):
        sys.exit()


if __name__ == '__main__':
    userObj = user.User('Lucas', 1234)
    try:
        userLoaded = data.Data().load_user(userObj.name, userObj.password)
        logging.debug('User succesfully loaded.')
        isLoaded = True
    # Using general except as I want here the program to continue, regardless
    # of what caused the error.
    except:
        logging.debug('User not loaded.')
        isLoaded = False

    if isLoaded:
        Menu(userLoaded)
    else:
        logging.debug('Saving and using created user.')
        notify_observers(userObj)
        Menu(userObj)