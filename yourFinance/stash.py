#! python3

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
                raise Exception('Wrong data type delivered to <amount> variable in "{}" Stash object.'.format(self.name))

    def set_name(self):
        name = input('Name of this money deposition place: ')
        self.name = name

    def set_amount(self):
        while True:
            amount = input('Amount stored in this money deposition place: ')
            try:
                self.amount = round(float(amount), 2)
                break
            except:
                print('Wrong type, please provide a number')
                continue

    def increase_amount(self, amount):
        self.amount = round(float(self.amount + amount), 2)

    def decrease_amount(self, amount):
        self.amount = round(float(self.amount - amount), 2)

    def show_stash(self):
        return '{}: {}'.format(self.name, self.amount)