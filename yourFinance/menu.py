#! python3

import sys
from yourFinance import data, user, year, month, stash


class Menu:
    """Shows options of the program."""
    def __init__(self, userObj):
        self.userObj = userObj
        mainChoices = {
            "1": self.add_month,
            "2": self.choose_time_to_display,
            "3": self.run_analyze_menu,
            "4": self.configure_settings,
            "5": self.exit,
        }
        self.display_menu = '''\nWelcome in yourFinance program. What would you like to do:
1. Add new data for the month.
2. Check data for the whole time, year or month.
3. Analyze data.
4. Configure settings.
5. Exit.
'''
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
            # To ensure that only main menu will be in loop. Other menus
            # should be viewed once and then come back to main menu.
            if textMenu != self.display_menu:
                break

    def add_month(self):
        """Lets user to input and save data for certain month."""
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
        year = input('Which year is it for? ')
        month = input('Which month is it for? ')
        try:
            print(self.userObj.yearDict[int(year)].monthDict[month].show_month())
        except:
            print('\nNo data in database for {} {}'.format(month, year))

        input('\nHit enter to go back to menu.')

    def display_year(self):
        year = input('Which year is it for? ')
        try:
            print(self.userObj.yearDict[int(year)].show_year())
        except:
            print('\nNo data in database for {}'.format(year))

        input('\nHit enter to go back to menu.')

    def display_all(self):
        print(self.userObj.show_funds())
        input('\nHit enter to go back to menu.')

    def run_analyze_menu(self):
        """Runs submenu with more options."""
        analyzeChoices = {
            "1": self.analyze_last_month,
            "2": self.analyze_chosen_month,
            }
        display_analyze_menu = '''\nWhat would you like to do:
        1. Analyze last month.
        2. Analyze chosen month.'''
        self.run(display_analyze_menu, analyzeChoices)

    def analyze_last_month(self):
        try:
            yearsList = list(self.userObj.yearDict.keys())
            yearsList.sort()
            yearObj = self.userObj.yearDict[yearsList[-1]]
            for monthName in reversed(month.Month.MONTHS_NAMES):
                if monthName in yearObj.monthDict.keys():
                    monthObj = yearObj.monthDict[monthName]
                    break
        except:
            input('No such data in your database. Hit enter. ')
            return

        self.analyze_month(yearObj.number, monthObj, True)

    def analyze_chosen_month(self):
        yearNumber = year.Year().number
        monthName = month.Month().name
        try:
            monthObj = self.userObj.yearDict[yearNumber].monthDict[monthName]
        except:
            input('No such data in database. Hit enter. ')
            return
        self.analyze_month(yearNumber, monthObj)

    def analyze_month(self, yearNumber, monthObj, isLastMonth=False):
        print('\n', yearNumber, '\n')
        print(monthObj.show_month())
        self.compare_previous_month(yearNumber, monthObj)
        self.check_monthly_costs(monthObj)
        if isLastMonth:
            self.subtract_current_costs(monthObj)
        input('\nHit enter to go back to menu.')

    def compare_previous_month(self, yearNumber, monthObj):
        """Compares given month with previous one, if there is one in data."""
        if monthObj.name == 'jan':
            prevYearNumber = yearNumber - 1
        else:
            prevYearNumber = yearNumber
        prevMonthName = month.Month.MONTHS_NAMES[
            month.Month.MONTHS_NAMES.index(
                monthObj.name)-1]
        print('Previous month is:\n')
        try:
            prevMonthObj = self.userObj.yearDict[
                      prevYearNumber].monthDict[
                      prevMonthName]
            print(prevMonthObj.show_month())
        except:
            print('No data in database for {} {} \n'.format(
                prevYearNumber,
                prevMonthName))
            return
        gain = monthObj.totalStash.amount - prevMonthObj.totalStash.amount
        if gain >= 0:
            print('You have gained: \n {}'.format(gain))
        else:
            print('You have lost: \n {} \n'.format(abs(gain)))

    def check_monthly_costs(self, monthObj):
        """Checks monthly costs for given month."""
        for key in self.userObj.mothlyCosts.keys():
            monthsVol = monthObj.totalStash.amount / userObj.mothlyCosts[key]
            print('Your sum is enough for '
                  + str(round(monthsVol, 1))
                  + ' months, based on '
                  + key + ' of '
                  + str(userObj.mothlyCosts[key])
                  + ' for total amount of ' +
                  str(monthObj.totalStash.amount))

    def subtract_current_costs(self, monthObj):
        monthTotality = monthObj.totalStash.amount
        costValueTotal = 0
        for cost in self.userObj.currentCosts:
            costValue = input('\nHow much you will spend this month on {}? '
                              .format(cost))
            monthTotality -= int(costValue)
            costValueTotal += int(costValue)
        print('\nYour total current costs are {}.'.format(costValueTotal))
        print('At the end of the month you will have {}.'.format(monthTotality))

    def configure_settings(self):
        """Gives options of settings to configure and save."""
        confChoices = {
            "1": self.configure_stashes_names,
            "2": self.configure_monthly_costs,
            "3": self.configure_current_costs,
        }
        display_conf_menu = '''\nWhat would you like to do:
        1. Configure names of money deposition places.
        2. Configure monthly costs names and amounts.
        3. Configure current costs groups.'''
        self.run(display_conf_menu, confChoices)


    def configure_stashes_names(self):
        self.configure_list_or_dictionary('money deposition places',
                                          self.userObj.stashNames)

    def configure_monthly_costs(self):
        self.configure_list_or_dictionary('monthly costs',
                                          self.userObj.mothlyCosts)

    def configure_current_costs(self):
        self.configure_list_or_dictionary('current costs',
                                          self.userObj.currentCosts)

    def configure_list_or_dictionary(self, dataName, configData):
        """Configures user data to use in program."""
        print('''\nThese are your {}:'''.format(dataName))
        if isinstance(configData, list):
            print(configData)
        elif isinstance(configData, dict):
            for key, value in configData.items():
                print(key + ':', value)
        choice = input("Hit enter to save it or 'change' to change it: ")
        if choice == '':
            return
        print('Please write new elements, hit enter to finish')
        if isinstance(configData, list):
            configData = []
            print('(please hit enter after each element)')
            while True:
                element = input()
                if element == '':
                    break
                configData.append(element)
        elif isinstance(configData, dict):
            configData = {}
            print('(please write name of element, hit enter, then its value)')
            while True:
                elementName = input()
                if elementName == '':
                    break
                elementValue = input()
                try:
                    elementValue = float(elementValue)
                except:
                    print('\nWrong data type, repeat element name and value')
                    continue
                configData[elementName] = elementValue
        print('These are your new {}. Hit enter to finish.'.format(dataName))
        if isinstance(configData, list):
            print(configData)
        elif isinstance(configData, dict):
            for key, value in configData.items():
                print(key + ':', value)
        # Adding data to user account and saving.
        if dataName == 'money deposition places':
            self.userObj.stashNames = configData
        elif dataName == 'monthly costs':
            self.userObj.mothlyCosts = configData
        elif dataName == 'current costs':
            self.userObj.currentCosts = configData
        data.Data().save_user(self.userObj)
        input()

    def exit(self):
        sys.exit()


if __name__ == '__main__':
    userObj = user.User('Lucas', 1234)
    try:
        userLoaded = data.Data().load_user(userObj.name, userObj.password)
        Menu(userLoaded)
    except:
        Menu(userObj)