#! python3
# analyze_menu.py - stores AnalyzeMenu class, which is subclass of
# Menu class. It holds submenu for analyzing certain month data.
from yourFinance import menu, year, month


class AnalyzeMenu(menu.Menu):
    """Shows analyze options of the program and performs actions."""
    def __init__(self, userObj):
        self.userObj = userObj
        analyzeChoices = {
            "1": self.analyze_last_month,
            "2": self.analyze_chosen_month,
        }
        display_analyze_menu = '''\nWhat would you like to do:
                1. Analyze last month.
                2. Analyze chosen month.'''
        # Uses run function, inherited from Menu class.
        self.run(display_analyze_menu, analyzeChoices)

    def analyze_last_month(self):
        """Checks which month is latest and runs analyze function with it."""
        try:
            yearsList = list(self.userObj.yearDict.keys())
            yearsList.sort()
            yearObj = self.userObj.yearDict[yearsList[-1]]
            for monthName in reversed(month.Month.MONTHS_NAMES):
                if monthName in yearObj.monthDict.keys():
                    monthObj = yearObj.monthDict[monthName]
                    break
        except IndexError:
            input('No such data in your database. Hit enter. ')
            return
        self.analyze_month(yearObj.number, monthObj, True)

    def analyze_chosen_month(self):
        """Asks which month to check and runs analyze function with it."""
        yearNumber = year.Year().number
        monthName = month.Month().name
        try:
            monthObj = self.userObj.yearDict[yearNumber].monthDict[monthName]
        except KeyError:
            input('No such data in database. Hit enter. ')
            return
        self.analyze_month(yearNumber, monthObj)

    def analyze_month(self, yearNumber, monthObj, isLastMonth=False):
        """Analayze given month."""
        print('\n', yearNumber, '\n')
        print(monthObj.show_month())
        self.compare_previous_month(yearNumber, monthObj)
        self.check_monthly_costs(monthObj)
        if isLastMonth:
            self.subtract_current_costs(monthObj)
        input('\nHit enter to go back to menu.')

    def compare_previous_month(self, yearNumber, monthObj):
        """Compares given month with previous one, if there is one in data."""
        # Separate situation for january, as it changes year as well.
        if monthObj.name == 'jan':
            prevYearNumber = yearNumber - 1
        else:
            prevYearNumber = yearNumber
        # Takes name of one month before given one.
        prevMonthName = month.Month.MONTHS_NAMES[
            month.Month.MONTHS_NAMES.index(
                monthObj.name)-1]
        print('Previous month is:\n')
        # Checks if there is data for previous month.
        try:
            prevMonthObj = self.userObj.yearDict[
                      prevYearNumber].monthDict[
                      prevMonthName]
            print(prevMonthObj.show_month())
        except KeyError:
            print('No data in database for {} {} \n'.format(
                prevYearNumber,
                prevMonthName))
            return
        # Checks the money difference between given and previous months.
        gain = round(monthObj.totalStash.amount
                     - prevMonthObj.totalStash.amount, 2)
        if gain >= 0:
            print('You have gained: \n {}'.format(gain))
        else:
            print('You have lost: \n {} \n'.format(abs(gain)))

    def check_monthly_costs(self, monthObj):
        """Checks for how long total sum of given month is enough."""
        for key in self.userObj.monthlyCosts.keys():
            monthsVol = monthObj.totalStash.amount\
                        / self.userObj.monthlyCosts[key]
            print('Your sum is enough for '
                  + str(round(monthsVol, 1))
                  + ' months, based on '
                  + key + ' of '
                  + str(self.userObj.monthlyCosts[key])
                  + ' for total amount of ' +
                  str(round(monthObj.totalStash.amount, 2)))

    def subtract_current_costs(self, monthObj):
        """Asks about current costs and provides the final sum."""
        monthTotality = round(monthObj.totalStash.amount, 2)
        costValueTotal = 0
        for cost in self.userObj.currentCosts:
            costValue = input('\nHow much you will spend this month on {}? '
                              .format(cost))
            if costValue == '':
                return
            try:
                monthTotality -= round(float(costValue), 2)
                costValueTotal += round(float(costValue), 2)
            except ValueError:
                print("\nInvalid input.")
                break
        print('\nYour total current costs are {}.'.format(costValueTotal))
        print('At the end of the month you will have {}.'.format(monthTotality))