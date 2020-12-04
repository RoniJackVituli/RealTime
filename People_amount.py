import module1
from Counter import stores_registered

obj = module1.open_data()
length = stores_registered()


def get_people_amount():
    for i in range(length):
        print('Number of people in ' + obj['Stores'][i]['Name'] + ' right now:')
        print((obj['Stores'][i]['Current_Amount']))


get_people_amount()
