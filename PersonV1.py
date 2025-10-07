class Person:
    def __init__(self, name, age=20):
        self.name = name
        self.age = age
    def __repr__(self):
        return f"{self.name} -> {self.age}"
    def __eq__(self, other):
        return self.age==other.age and self.name==other.name
    
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
