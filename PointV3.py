import re
class Point: 
    
    counter=0 # a "class variable"
    
    def __init__(self, valx, valy):
        self.x=valx # x is a "data attribute" or "instance variable"
        self.y=valy
        Point.counter += 1
        
    def __repr__(self):
        return f"<{self.__x},{self.y}>"
    
    def __str__(self):
        return f"<{self.__x},{self.y}>"
    
    def __del__(self):
        Point.counter -= 1
        
    def clear(self):
        self.__x=self.__y=0
        
    def __eq__(self, other): # ==
        return self.__x == other.__x and self.y ==other.y
    
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, valx):
        if isinstance(valx, int):
            self.__x=valx
        else:
            raise Exception ("Wrong value for x")
    
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, valy):
        if isinstance(valy, int):
            self.__y=valy
        else:
            raise Exception ("Wrong value for y")
            
    # parsePoint is a "class" or "static" method:
    @staticmethod
    def parsePoint(text):
        regexp=re.compile(r"<(\d+),(\d+)>")
        mo=regexp.match(text)
        if mo:
            return Point(int(mo.group(1)), int(mo.group(2)))
        else:
            return Point(0,0)
        
    #parsePoint=staticmethod(parsePoint)  
    
c=Point.parsePoint("<23,56>")
print(c) # <23,56>

print(Point.counter)
c1=Point(2,5)
print(c1)
print(Point.counter)

del c1
print(Point.counter)




