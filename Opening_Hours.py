import json
import module1
num_of_stores = 3


obj = module1.open_data()

def opening_hours():
    for i in range(num_of_stores):
        print('Opening hours of ' + obj['Stores'][i]['Name'] + ':')
        print((obj['Stores'][i]['Hours']))


