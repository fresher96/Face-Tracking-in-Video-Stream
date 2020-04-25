
import json;

def readConfigs():
	with open('configs.json', 'r') as f:
		return json.load(f);

# print(readConfigs());
