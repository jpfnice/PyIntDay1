
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
    
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, valx):
        if isinstance(valx, int):
            self.__x=valx
        else:
            raise Exception ("Wrong value for x")

    """
    x=property(getX, setX)
        is equivalent to:
    x=property(getX)
    x.setter(setX)
    """
    
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, valy):
        if isinstance(valy, int):
            self.__y=valy
        else:
            raise Exception ("Wrong value for y")
    
    def __setattr__(self,name,value):
        if name not in ["x","y", "_Point__x", "_Point__y"]:
            raise Exception(f"Wrong name {name}")
        super().__setattr__(name, value)
    
c=Point(2,3)
print(c)
print(c.__dict__)

c.x=78 # => c.setX(78)


print(c)

"""

obj.x=23

1) obj.__setattr__("x", 23)
2) use of property
"""    