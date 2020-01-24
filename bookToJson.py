import json

f = open("INTRODUCTION.txt", "r")

data = f.read()

with open('data.json', 'w') as f:
	json.dump(data, f)