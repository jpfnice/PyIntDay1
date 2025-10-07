import json

with open("data.json", "r") as f:
    newd=json.load(f)
    
print(newd, type(newd))