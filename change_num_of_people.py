import json

with open('data.json', 'r') as f:
    data = f.read()
obj = json.loads(data)

print(obj['Stores'])

Stores = json.opendata()

def change_num_of_people():
    name = input('Enter name of store')
    for i in range (3):
        if Stores[i]["Name"] == name:
            num = input('Enter new number of allowed people')
            Stores[i]["Allowed_People"] = num


