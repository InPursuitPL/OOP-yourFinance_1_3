#! python3
from yourFinance import menu, data, user, year, month, stash

def login():
    name = input('Please type in your username and hit enter: ')
    password = input('Please type in your password and hit enter: ')
    try:
        return data.Data().load_user(name, password)
    except:
        print('Wrong username or password.')
        return None

def new_user():
    name = input('Please type in chosen username and hit enter: ')
    password = input('Please type in chosen password and hit enter: ')
    newUserObj = user.User(name, password)
    data.Data().save_user(newUserObj)
    return newUserObj

print('Welcome in yourFinance program.\n')

while True:
    decision = input('Please choose "Sign in" or "New user": ')
    if decision.lower().startswith('sig'):
        userObj = login()
        if userObj:
            break
        else:
            continue
    elif decision.lower().startswith('new'):
        userObj = new_user()
        break
    else:
        print('I did not understand, please try again.')
        continue



