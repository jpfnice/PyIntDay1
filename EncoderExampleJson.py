import json

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f"{self.name} -> {self.age}"


def person_encoder(obj):
  if isinstance(obj, Person):
     return {"name": obj.name, "age": obj.age}
 
    
p1=Person("Jean", 24)
print(p1)

with open("data.json", "w") as f:
    json.dump(p1, f, default=person_encoder)


