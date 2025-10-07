
"""
Given a file (you can use "measures.txt", see the github repo) with the following format:
    
    City name;time;date;temperature
    Geneva;12:34;2003/12/23;2.34;
    Lausanne;12:36;2003/12/23;3.34;
    Bern;12:36;2003/12/23;-3.34;
    ....
    
Write a python script to parse this file and store it's content into a "custom object".

You could define a class "Record" that will represent a line of this file and
a class "ListOfRecord" to represent a list of "Record".

This class "ListOfRecord" should offer:

a way to construct an instance of it with the help of a text file like the one above.

a ways to save/restore the list easily (using pickle)

a method to compute the average of the temperature recorded for a given city name.

any other method you consider interesting to provide: for instance a method to compute the minimum and maximum of the temperatures recorded for a given city name.

"""
import pickle
class Record:
    
    def __init__(self, name, time, date, temp):
        self.city=name 
        self.time=time
        self.date=date
        self.temperature=temp
    
    def __str__(self): # __str__() makes use of __repr__()
        return self.__repr__()
    
    def __repr__(self):
        return f"{self.city} at {self.date} {self.time}: {self.temperature}"
    
    # Note: classmethod is equivalent to staticmethod the only difference is that a
    # classmethod get an implicit argument: the class the method belongs to
    
    @classmethod
    def parse(cls, text):
        #Geneva;12:34;2003/12/24;6.84
        c,t,d,temp=text.split(";")
        return Record(c, t, d, float(temp))
    
    def temperatureGet(self):
        return self.__temperature 
       
    def temperatureSet(self, val):
        if not isinstance(val, float):
            raise Exception("Wrong kind of temperature")
        self.__temperature=val
    
    temperature=property(fget=temperatureGet, fset=temperatureSet) 
    
    # NOTE: city, time and date could (and should) also be defined as properties ...       
           
class ListOfRecord:
        
    def __init__(self):
        self.data=[] 
       
    def __repr__(self):
        return str(self.data)
    
    # __str__() is invoked when you print an object with the print function. 
    # In case __str__() is missing, then print and any function using str() 
    # invokes __repr__() of object. 
    
    # __str__() of containers, when invoked, will execute __repr__() 
    # method of its contained elements.
    
    def __str__(self): # __str__() makes use of __repr__()
        return self.__repr__()  
    
    def addRecord(self, record):
        self.data.append(record)
        
    @classmethod
    def parseFile(self, fname):
        lr=ListOfRecord()
        with open(fname,"r") as fic:
            fic.readline()
            for line in fic:
                lr.addRecord(Record.parse(line))
        return lr  
         
   
    @classmethod
    def load(self, fname):
        with open(fname, "rb") as f:
            return pickle.load(f)
            
     
    def save(self, fname):
        with open(fname, "wb") as f:
            pickle.dump(self, f)
            
    def __contains__(self, city): # associated with the "in" operator
        for r in self.data:
            if r.city == city:
                return True
        return False 
            
    def averageTemp(self, cityName):
        if not cityName in self:
            raise Exception (f"{cityName} is not in the list")
        total=0
        ix=0
        for r in self.data: 
            if r.city==cityName:
                ix += 1
                total += r.temperature 
        return total/ix   
    
    def minMax(self, cityName):
        if not cityName in self:
            raise Exception (f"{cityName} is not in the list")
        first=True
        for r in self.data:
            if r.city==cityName:
                if first:
                    mini=maxi=r.temperature
                    first=False
                else:
                    if r.temperature > maxi: maxi=r.temperature
                    if r.temperature < mini: mini=r.temperature
        return (mini, maxi)
        
    def minMaxAll(self):
        first=True
        for r in self.data:
            if first:
                mini=maxi=r.temperature
                first=False
            else:
                if r.temperature > maxi: maxi=r.temperature
                if r.temperature < mini: mini=r.temperature
        return (mini, maxi)  
        
if __name__ == "__main__":
 
    
    lofr=ListOfRecord.parseFile("measures.txt")

    print(lofr)        
    
    lofr.save("lor.pick")
    
    lofrBis=ListOfRecord.load("lor.pick")
    print(lofrBis) 
    
    city="Geneva"
    result=lofr.averageTemp(city)
    print(result)
  
    result=lofr.minMax(city)
    print("Mini, maxi:", result)
   
    

