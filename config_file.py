
import json;

def readConfigs():
	with open('configs.json', 'r') as f:
		configs = json.load(f);
	
	if(configs['colab'] == 'True'):		
		with open('configs_colab.json', 'r') as f:
			configs = json.load(f);
	
	return configs;

# print(readConfigs());
