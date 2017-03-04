#! python3
# menu.py - main menu for yourFinance program. Can be tested as script,
# without logging through main.py module.
import sys
import logging

from yourFinance import data, user, year, month, stash

logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)


class Menu:
    """Shows options of the program."""
    # Leave it as class attribute to let it be inherited.
    display_menu = '''\nWelcome in yourFinance program. What would you like to do:
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
            "2": self.choose_time_to_display,
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
        data.Data().save_user(self.userObj)

        print('\nData for year {} saved:'.format(yearObj.number))
        print(yearObj.monthDict[monthObj.name].show_month())
        input('\nHit enter to go back to menu.')

    def choose_time_to_display(self):
        """User can decide which part of data he wants to display."""
        timeChoices = {
            "1": self.display_month,
            "2": self.display_year,
            "3": self.display_all
        }
        display_time_menu = '''Which part of data you would like to see:
        1. Certain month
        2. Certain year
        3. All data in database'''
        self.run(display_time_menu, timeChoices)


    def display_month(self):
        """Displays month after user input."""
        year = input('Which year is it for? ')
        month = input('Which month is it for? ')
        try:
            print(self.userObj.yearDict[int(year)].monthDict[month].show_month())
        except:
            print('\nNo data in database for {} {}'.format(month, year))

        input('\nHit enter to go back to menu.')

    def display_year(self):
        """Displays year after user input."""
        year = input('Which year is it for? ')
        try:
            print(self.userObj.yearDict[int(year)].show_year())
        except:
            print('\nNo data in database for {}'.format(year))

        input('\nHit enter to go back to menu.')

    def display_all(self):
        """Displays all time data for this user."""
        print(self.userObj.show_funds())
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
        Menu(userLoaded)
    except:
        logging.debug('User not loaded. Using created user.')
        Menu(userObj)