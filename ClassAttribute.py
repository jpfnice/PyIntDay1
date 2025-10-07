import re
class Point: # __new__(), __init__(), __eq__()
    
    counter=0 # A class attribute
    
    def __init__(self, valx, valy): # The "constructor"
        self.__x=valx
        self.__y=valy
        Point.counter += 1
        
    def __del__(self):
        Point.counter -= 1
    
    def parsePoint(self, data):
        reg=re.compile(r"^<(\d+),(\d+)>$") # data could be "<15,6>"
        mo=reg.search(data)
        if mo:
            return Point(int(mo[1]), int(mo[2]))
        else:
            raise Exception("Invalid string received")
            
    # parsePoint is defined as a class method:        
    parsePoint=classmethod(parsePoint) 
     
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

print(Point.counter)    
p1=Point(2,2)
print(Point.counter)  
p2=Point(1,4)
print(Point.counter)  
del p1
print(Point.counter)  

center=Point.parsePoint("<0,0>")
print(center)


