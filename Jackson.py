import json
with open('./JAckson.json') as f:
  data = json.load(f)
print(data)