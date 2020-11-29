import json

def open_data():
	with open('data.json','r') as f:
		data = f.read()
	obj = json.loads(data)
	return obj


def print_data():
	
	obj = open_data()
	print()
	print("Stores:")
	print()
	for i in range(3):
		print(obj["Stores"][i]["Name"])
		print("Working hours: ", obj["Stores"][i]["Hours"])
		print("Amount of people allowed: ",obj["Stores"][i]["Allowed_People"])
		print(obj["Stores"][i]["Product_types"])
		print()
