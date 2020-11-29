import json

with open('data.json','r') as f:
	data = f.read()
obj = json.loads(data)

print(obj['Stores'])
