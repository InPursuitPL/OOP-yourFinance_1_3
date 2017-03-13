#! python3
# main.py - main file that starts yourFinance program. Here you can log
# in or create new user that will be transferred to the next part of the
# program.
from yourFinance import menu, data, user


def return_user_obj_or_None(name, password, isNew):
    """Provides user object or None if user not found in database."""
    if isNew:
        newUserObj = user.User(name, password)
        menu.notify_observers(newUserObj)
        return newUserObj
    else:
        try:
            return data.Data().load_user(name, password)
        except Exception:
            return


if __name__ == '__main__':
    print('''Welcome in yourFinance program.

    This program helps you to manage your budget.
    It saves budget data as separate money deposition places
    for certain month and certain year. You can check detailed
    data as well as analyze certain month to see the values
    and other information.''')
    while True:
        decision = input('\nPlease choose "Sign in" or "New user": ')
        if decision.lower().startswith('sig'):
            isNew = False
        elif decision.lower().startswith('new'):
            isNew = True
        else:
            print('I did not understand, please try again.')
            continue
        name = input('Please type in username and hit enter: ')
        password = input('Please type in password and hit enter: ')
        userObj = return_user_obj_or_None(name, password, isNew)
        if userObj:
            break
        print('Wrong username or password.')
        continue
    # Starts main menu with given user object as attribute.
    menu.Menu(userObj)


