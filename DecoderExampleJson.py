import json

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f"{self.name} -> {self.age}"


def person_decoder(obj):
  if "name" in obj and "age" in obj:
     return Person(obj["name"], obj["age"])
 
    
 
with open("data.json", "r") as f:
    newd=json.load(f, object_hook=person_decoder)
    
print(newd, type(newd))

