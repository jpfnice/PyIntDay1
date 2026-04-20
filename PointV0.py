

class Point: # __new__() __init__() __repr__() __eq__()

    def __init__(self, valx, valy): # __init__ is the "constructor"
        self.x=valx # x is an "attribute"
        self.y=valy
    def __repr__(self):
        return f"<{self.x}, {self.y}>"
    def __eq__(self, other):
        return self.x==other.x and self.y==other.y
    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)
    def reset(self):
        self.x=0
        self.y=0
        
        
# A constructor call:
    
p1=Point(2, 3)
# 1) p1=Point.__new__() # to allocate memory space
# 2) p1.__init__(2, 3) # to initialize the memory space allocated
# 3) __init__(p1, 2, 3)

print("x of p1 is", p1.x)
print("y of p1 is", p1.y)

p1.x=p1.x + 5
print("x of p1 is", p1.x)

print(p1)
# 1) print(p1.__repr__()))

p0=Point(7, 5)
print(p0)

print(p1 == p0) # -> print(p1.__eq__(p0))

p2=p0+p1 # -> print(p1.__add__(p0))
print(p2)

p2.reset()
print(p2)



# l1=list()
# l1.append(56)
# print(l1)

# Example of constructor call:
    
# l=list() # l=[]
# text=str()

# import datetime

# today=datetime.date(2026,4,20)
# print(today)
