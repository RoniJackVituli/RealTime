import module1
from Counter import stores_registered


length = stores_registered()
obj = module1.open_data()


def opening_hours():
    for i in range(length):
        print('Opening hours of ' + obj['Stores'][i]['Name'] + ':')
        print((obj['Stores'][i]['Hours']))
    return True
