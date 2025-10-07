import dataclasses 

@dataclasses.dataclass
class Person:
    name: str
    age: int = 20
    
    
p1=Person("Mario",24)
print(p1)
print(p1.age)
p1.age=45
print(p1)
p1=Person("Mario",23)
p2=Person("Mario",23)
print(p2)
print(p1==p2)

p3=Person("Flavio")
print(p3)
