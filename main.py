#! python3
#main.py - main file that starts yourFinance program. Here you can log
#in or create new user that will be transferred to the next part of the
#program.
from yourFinance import menu, data, user, year, month, stash

def return_user_obj_or_None(name, password, isNew):
    '''Provides user object or None if user not found in database.'''
    if isNew:
        newUserObj = user.User(name, password)
        data.Data().save_user(newUserObj)
        return newUserObj
    else:
        try:
            return data.Data().load_user(name, password)
        except:
            return None


if __name__ == '__main__':
    print('Welcome in yourFinance program.\n')
    while True:
        decision = input('Please choose "Sign in" or "New user": ')
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

    menu.Menu(userObj)


