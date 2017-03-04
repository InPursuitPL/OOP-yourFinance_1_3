#! python3
# configure_menu.py - stores ConfigureMenu class, which is subclass of
# Menu class. It holds submenu for configuration some user values with
# names for default money stashes and so on.
from yourFinance import menu, data


class ConfigureMenu(menu.Menu):
    """Shows configuration options of the program and performs actions."""
    def __init__(self, userObj):
        self.userObj = userObj
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
        """Redirects to combined function."""
        self.configure_list_or_dictionary('money deposition places',
                                          self.userObj.stashNames)

    def configure_monthly_costs(self):
        """Redirects to combined function."""
        self.configure_list_or_dictionary('monthly costs',
                                          self.userObj.mothlyCosts)

    def configure_current_costs(self):
        """Redirects to combined function."""
        self.configure_list_or_dictionary('current costs',
                                          self.userObj.currentCosts)

    def configure_list_or_dictionary(self, dataName, configData):
        """Configures user data. Input can be list or dict."""
        # Prints elements in given data.
        print('''\nThese are your {}:'''.format(dataName))
        if isinstance(configData, list):
            print(configData)
        elif isinstance(configData, dict):
            for key, value in configData.items():
                print(key + ':', value)
        # Asks if change values and leaves function if not.
        choice = input("Hit enter to save it or 'change' to change it: ")
        if choice == '':
            return
        # Asks about new elements to put into data.
        print('Please write new elements, hit enter to finish')
        # Part for list type data.
        if isinstance(configData, list):
            configData = []
            print('(please hit enter after each element)')
            while True:
                element = input()
                if element == '':
                    break
                configData.append(element)
        # Part for dictionary type data.
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
        # Prints new data values.
        print('These are your new {}. Hit enter to save.'.format(dataName))
        if isinstance(configData, list):
            print(configData)
        elif isinstance(configData, dict):
            for key, value in configData.items():
                print(key + ':', value)
        # Adding data to user account and saving updated user.
        if dataName == 'money deposition places':
            self.userObj.stashNames = configData
        elif dataName == 'monthly costs':
            self.userObj.mothlyCosts = configData
        elif dataName == 'current costs':
            self.userObj.currentCosts = configData
        data.Data().save_user(self.userObj)
        input()