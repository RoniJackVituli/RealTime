import json
import module1

obj = module1.open_data()

def opening_hours(store_name):
    if store_name == 'ZARA':
        print('Opening hours of ' + store_name + ':')
        print((obj['Stores'][0]['Hours']))
    elif store_name == 'Pull & Bear':
        print('Opening hours of ' + store_name + ':')
        print((obj['Stores'][1]['Hours']))
    elif store_name == 'H&M':
        print('Opening hours of ' + store_name + ':')
        print((obj['Stores'][2]['Hours']))
    else:
        print('Store not found')
