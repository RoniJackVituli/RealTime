name_company = "RealTime"
name_owner = "Roni Jack Vituli"
StrPassword = "5t4r3e2w1q"

def update_activity_time():

def check_password(strPass):
    if password == strPass:
        return True
    return False

def check(str):
    with open('Test.txt') as f:
        if str in f.read():
            return True
    return False

def switch_demo(argument):
    switcher = {
        1: ""
    }

def check_user_company(user,company):
    if check(user) and check(company):
        return True
    return False

flag = False

while(not flag):
    user_name = input('Enter your name: ')
    company = input('Enter the name of the company you work: ')
    if(check_user_company(user_name,company)):
        flag = True
    else:
        print("Worng input please try again")

flag = False
while(not flag):
    password = input("Hey {0}, Please enter your password: ".format(user_name))
    if(check_password(password)):
        flag = True
    else:
        print("Worng Password, please enter again")

