import json

with open('data.json', 'r') as f:
    data = f.read()
obj = json.loads(data)


def opening_hours():
    for i in range(3):
        print('Opening hours of ' + obj['Stores'][i]['Name'] + ':')
        print((obj['Stores'][i]['Hours']))
