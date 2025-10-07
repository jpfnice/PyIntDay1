class Point: # __new__(), __init__(), __eq__(), __setattr__() 
    def __init__(self, valx, valy): # The "constructor"
        self.x=valx
        self.y=valy
    def clear(self):
        self.x=0
        self.y=0
    def __str__(self): # used to convert a point into a str
        return f"<{self.x},{self.y}>"
    def __repr__(self): # used to convert a point into a str
        return f"<{self.x},{self.y}>"
    def __eq__(self, other): # invoked when you use ==
        return self.x==other.x and self.y==other.y
    def __add__(self, other): # invoked when you use +
        return Point(self.x+other.x, self.y+other.y)
    def setX(self, valx):
        if isinstance(valx, int):
            self.x=valx
        else:
            raise Exception ("Wrong value for x")
    def setY(self, valy):
        if isinstance(valy, int):
            self.y=valy
        else:
            raise Exception ("Wrong value for y")
    def getX(self):
        return self.x
    def getY(self):
        return self.y

p=Point(2,2)
del p.x
print(p)
#print(p)


# 1) p=Point.__new__()
# 2) p.__init__(2,2) => __init__(p,2,2)
# print(p.__dict__)
# p.x=5
# print(p.__dict__)

# p.X=8
# print(p.__dict__)

# #del p.x
# print(p)

# p.setX(8)
# p.x="abc"

# print(p)
# # 1) print(str(p)))
# # 2) print(p.__repr__()))
# p.clear()
# print(p)

# p1=Point(0,3)
# p2=p+p1
# # p2=p.__add__(p1)

# l=[Point(5,6), Point(7,8)]
# print(l)
