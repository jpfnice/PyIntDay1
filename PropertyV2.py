class Point: # __new__(), __init__(), __eq__(), __setattr__() 
    def __init__(self, valx, valy): # The "constructor"
        self.__x=valx
        self.__y=valy
    def clear(self):
        self.__x=0
        self.__y=0
    def __str__(self): # used to convert a point into a str
        return f"<{self.__x},{self.__y}>"
    def __repr__(self): # used to convert a point into a str
        return f"<{self.__x},{self.__y}>"
    def __eq__(self, other): # invoked when you use ==
        return self.__x==other.__x and self.__y==other.__y
    def __add__(self, other): # invoked when you use +
        return Point(self.__x+other.__x, self.__y+other.__y)
    
    def setX(self, valx):
        if isinstance(valx, int):
            self.__x=valx
        else:
            raise Exception ("Wrong value for x")
    def setY(self, valy):
        if isinstance(valy, int):
            self.__y=valy
        else:
            raise Exception ("Wrong value for y")
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    
    x=property(getX, setX)
    y=property(getY, setY)
    
p=Point(2,2)
print(p)
p.x=23
p.y=10# <=> p.setY(10)
del p.x
print(p.x) # <=> print(p.getX()) 
