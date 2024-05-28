
class Point: # __new__(), __init__(), __eq__(), __setattr__() 
    def __init__(self, valx, valy):
        self.x=valx # x is a "data attribute" or "instance variable"
        self.y=valy
    
    def __repr__(self):
        return f"<{self.__x},{self.__y}>"
    
    def clear(self):
        self.__x=self.__y=0
    
    def __eq__(self, other): # ==
        return self.__x == other.__x and self.__y ==other.__y
    
    def setX(self, valx):
        if isinstance(valx, int):
            self.__x=valx
        else:
            raise Exception ("Wrong value for x")
    
    def getX(self):
        return self.__x
    
    x=property(getX, setX)
    """
    x=property(getX, setX)
        is equivalent to:
    x=property(getX)
    x.setter(setX)
    """
    
    def setY(self, valy):
        if isinstance(valy, int):
            self.__y=valy
        else:
            raise Exception ("Wrong value for y")
    def getY(self):
        return self.__y
    
    y=property(getY, setY)
    
    def __setattr__(self,name,value):
        if name not in ["x","y", "_Point__x", "_Point__y"]:
            raise Exception(f"Wrong name {name}")
        super().__setattr__(name, value)
    
c=Point(2,3)
print(c)
print(c.__dict__)

c.x=78 # => c.setX(78)
c.Z=9

print(c)

"""

obj.x=23

1) obj.__setattr__("x", 23)
2) use of property
"""    