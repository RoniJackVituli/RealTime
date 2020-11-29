import json
from datetime import datetime
with open('data.json','r') as f:
    data = f.read()
obj = json.loads(data)

def check_account():
    for i in range (len(obj['Managers'])):
        if(obj['Managers'][i]['Name'] == account and obj['Managers'][i]['Password'] == password and obj['Managers'][i]['Store'] == store):
         return True
    return False

def update_open_hours():
    print("The correct hours is: ",store['Hours_Open'])
    store['Hours_Open'] = input('Enter new open Houres: ')

def menu_option(x):
    switcher = {
        0: update_open_hours,
    }
    return switcher.get(x, lambda: "invalid choice")


def Take_info_stroe():
    global store
    for i in range(len(obj['Stores'])):
        if(obj['Stores'][i]['Name'] == store):
            store = obj['Stores'][i]

def print_menu():
    global flag
    flag = False
    Take_info_stroe()
    hour = datetime.now().hour
    choice = 1
    while (not flag and choice != 0):
        print("\n\nÏ--------------------Hey {0}, Welcome to the management area--------------------".format(account))
        print("1. Change opening hours press -> 1")
        print("2. Exit from the programming -> 0")
        choice = int(input())
        menu_option(choice - 1)()
    if hour >= 5 and hour <= 12:
        print("All changes have been made\nGood Morning, {0}".format(account))
    elif hour > 12 and hour < 17:
        print("All changes have been made\nGood After noon, {0}".format(account))
    else:
        print("All changes have been made\nGood Evening, {0}".format(account))

def START():
    print("--------------------Welcome to RealTime--------------------")
    flag = False
    store = input('Enter the name of the store: ')
    account = input('Enter your name: ')
    password = input('Enter your password: ')
    while(not check_account()):
        print('Worng input please try again')
        store = input('Enter the name of the store: ')
        account = input('Enter your name: ')
        password = input('Enter your password: ')
    print_menu()