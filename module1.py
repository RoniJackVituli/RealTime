import json


def open_data():
    with open('data.json', 'r') as f:
        data = f.read()
    obj = json.loads(data)
    return obj