import json

with open('data.json', 'r') as f:
    data = f.read()
obj = json.loads(data)

print(obj['Stores'])

def change_num_of_people():
    name = input('Enter name of store')
    for i in range (3):
        if obj['Stores']["Name"] == name:
            num = int(input('Enter new number of allowed people'))
            obj['Stores']["Allowed_People"] = num