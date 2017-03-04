#! python3
# stash.py - stores Stash class. Stash object is month's money deposition
# place with given name and amount.


class Stash:
    def __init__(self, name='', amount=''):
        if name == '':
            self.set_name()
        else:
            self.name = name
        if amount == '':
            self.set_amount()
        else:
            try:
                self.amount = round(float(amount), 2)
            except:
                raise Exception('Wrong data type delivered to <amount>\
                 variable in "{}" Stash object.'.format(self.name))

    def set_name(self):
        """Sets stash name if it was not given while being created."""
        name = input('Name of this money deposition place: ')
        self.name = name

    def set_amount(self):
        """Sets stash amount if it was not given while being created."""
        while True:
            amount = input('Amount stored in {}: '.format(self.name))
            try:
                self.amount = round(float(amount), 2)
                break
            except:
                print('Wrong type, please provide a number')
                continue

    def increase_amount(self, amount):
        """Increases and rounds amount."""
        self.amount = round(float(self.amount + amount), 2)

    def decrease_amount(self, amount):
        """Decreases and rounds amount."""
        self.amount = round(float(self.amount - amount), 2)

    def show_stash(self):
        """Returns string with stash name and amount."""
        return '{}: {}'.format(self.name, round(self.amount, 2))