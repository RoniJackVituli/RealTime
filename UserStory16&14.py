#Roni Jack Vituli, ID 315369967

import json
from datetime import datetime
with open('data.json','r') as f:
    data = f.read()
obj = json.loads(data)
flag = False
AMOUNT_MANAGER = 3

#-------------------------------------------------Functions-------------------------------------------------
def check_account():
    for i in range (AMOUNT_MANAGER):
        if(obj['Managers'][i]['Name'] == account and obj['Managers'][i]['Password'] == password and obj['Managers'][i]['Store'] == store):
            return True
    return False

def update_open_hours():
    print("The correct hours is: ", store['Hours_Open'])
    store['Hours_Open'] = input('Enter new open Houres: ')

def Exit():
    print("All changes have been made")

def change_password():
    global account
    new_password = ''
    def same_password(str,index):
        if(str == obj['Managers'][index]['Password']):
            return True
        return False
    i = AMOUNT_MANAGER
    for i in range(AMOUNT_MANAGER):
        if obj['Managers'][i]['Name'] == account:
            new_password = input('Enter a new password: ')
            while(same_password(new_password,i)):
                new_password = input('The password was used in the past\nplease enter a new one: ')
        obj['Managers'][i]['Password'] = new_password

def menu_option(x):
    switcher = {
        -1: Exit,
        0: update_open_hours,
        1: change_password,
    }
    return switcher.get(x, lambda: print("invalid choice"))


def Take_info_stroe():
    global store
    for i in range(len(obj['Stores'])):
        if(obj['Stores'][i]['Name'] == store):
            store = obj['Stores'][i]

def print_menu():
    Take_info_stroe()
    hour = datetime.now().hour
    choice = 1
    while (choice != 0):
        print("\n\nֿ--------------------Hey {0}, Welcome to the management area--------------------".format(account))
        print("1. Change opening hours press -> 1")
        print("2. Change your password press -> 2")
        print("3. Exit from the programming -> 0")
        choice = int(input())
        menu_option(choice - 1)()
    if hour >= 5 and hour <= 12:
        print("Good Morning, {0}".format(account))
    elif hour > 12 and hour < 17:
        print("Good After noon, {0}".format(account))
    else:
        print("Good Evening, {0}".format(account))
#---------------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------START---------------------------------------------------------------------------------------------

print("--------------------Welcome to RealTime--------------------")
store = input('Enter the name of the store: ')
account = input('Enter your name: ')
password = input('Enter your password: ')
while(not check_account()):
    print('Worng input please try again')
    store = input('Enter the name of the store: ')
    account = input('Enter your name: ')
    password = input('Enter your password: ')

print_menu()





