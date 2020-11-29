import json

with open('data.json', 'r') as f:
    data = f.read()
obj = json.loads(data)

print(obj['Stores'])


def change_num_of_people():
    n = input('Enter new number of allowed people')
    return n


numberofallowedpeople = change_num_of_people()


def print_num_of_allowed_people():
    print('The maximum number of people in the store is {0}'.format(numberofallowedpeople))


