#! python3
# changelog.py - stores Changelog class, which manages changelog file.

import datetime
from yourFinance import data


class Changelog:
    def update(self, userObj):
        """Initializes update for changelog file."""
        self.save_change(userObj)

    def save_change(self, userObj):
        """Saves change in changelog with added formating and date info."""
        userString = '{}\n{}\n{}\n{}'.format(
            userObj.stashNames,
            userObj.currentCosts,
            userObj.monthlyCosts,
            userObj.show_funds())

        FILENAME = data.Data.FILENAME
        now = datetime.datetime.now()
        timeNowString = now.strftime('%Y/%m/%d %H:%M:%S')

        logFile = open('{}{}.txt'.format(FILENAME, '_changelog'), 'a')
        logFile.write('\n#####USER: {} TIME: {} #####\n{}'.format(
            userObj.name,
            timeNowString,
            userString))
        logFile.close()



