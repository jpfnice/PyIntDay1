'''
1)  Write 2 functions: parseDate and parseTime 

    parseDate() will take a string as argument representing a date  
    and will convert it (if possible) into a datetime.date object
    The accepted format could be: dd/mm/yyyy and dd/mm/yy (in this case we 
    assume yy is a year of the 21th century)
    Ex: 31/05/2019 or 31/05/19
    
    parseTime() will take a string as argument representing a time and will convert 
    it (if possible) into a datetime.time object
    The accepted format could be: hh:mm or hh:mm:ss or hhHmmMss or hhhmmmss
    Ex: 12:45 or 13:33:54 or 12H45M56 or 12h45m56
    
    If the string format is not correct, these functions should raise an exception
    
2)  Write a function parseFloat that do verify that a string received as argument 
    represent a valid float:
    
    examples of valid floats: 23.45 -3.4 +0.3 10. 0.
    examples of invalid floats: abc 002.3  10  0
    
    If the string represents a valid float the function will return the converted float 
    value otherwise it will raise an exception
    
    Note:     In a regexp a . means "any character except \n"
              In a regexp a \. means "the character ."
'''

import re
import datetime as dt 

# Definition of 3 new categories of Exceptions (this is simply an option you
# can limit yourself to the use of predefined exceptions: Exception, ValueError, ...):
    
class ParseDateError(Exception):
    pass

class ParseTimeError(Exception):
    pass 
 
class ParseFloatError(Exception):
    pass 

def isDate(inputText):
    reg=re.compile(r"""^          # beginning of the string
                       ([0-3]\d)  # the day
                       /
                       ([01]\d)   # the month
                       /
                       (\d\d|\d{4}) # the year
                       $            # end of the string
                       """, re.VERBOSE)
    
    mo=reg.search(inputText)
    return bool(mo)
    
def isTime(inputText):
    reg=re.compile(r"^([0-2]\d)[H:]([0-5]\d)([M:]([0-5]\d))?$", re.IGNORECASE)
    mo=reg.search(inputText)
    return bool(mo) 

def isFloat(inputText):
    reg=re.compile(r"^[+-]?(\d|[1-9]\d+)\.\d*$") 
    mo=reg.search(inputText)
    return bool(mo)
        
def parseDate(inputText):
    """
    documentation string or docstring
    Parameters
    ----------
    inputText : a string representing a date

    Raises
    ------
    ParseDateError if the argument received is not a valid date

    Returns
    -------
    A date object (constructed with the help of the argument received)

    """
    reg=re.compile(r"""^            # beginning of the string
                       ([0-3]\d)    # the day
                       /
                       ([01]\d)     # the month
                       /
                       (\d{2}|\d{4}) # the year
                       $            # end of the string
                       """, re.VERBOSE)
    
    mo=reg.search(inputText)
    if mo:
        #d,m,y=map(int, mo.groups())
        d=int(mo.group(1)) # d=int(mo[1])
        m=int(mo.group(2))
        y=int(mo.group(3))
        
        if y <= 99: 
            y += 2000
        return dt.date(y, m, d)
    else:
        raise ParseDateError(f"Wrong date value: {inputText} !") # >= 3.6
    
def parseTime(inputText):
    
    reg=re.compile(r"^([0-2]\d)[H:]([0-5]\d)([M:]([0-5]\d))?$", re.IGNORECASE)
    mo=reg.search(inputText)
    if mo:
        #print(mo.groups())
        hh,mm,__,sec=mo.groups() # unpacking
        if sec==None: 
            sec=0
        return dt.time(int(hh), int(mm), int(sec))
    else:
        raise ParseTimeError("Bad time format: {}".format(inputText)) # > 3.0

# def parseTime(inputText):
#     # (?: ... ) define a "non capturing group"
    
#     reg=re.compile(r"^([0-2]\d)[H:]([0-5]\d)(?:[M:]([0-5]\d))?$", re.IGNORECASE)
#     mo=reg.search(inputText)
#     if mo:
#         print(mo.groups())
#         hh,mm,sec=mo.groups()
#         if sec==None: sec=0
#         return dt.time(int(hh), int(mm), int(sec))
#     else:
#         raise ParseTimeError("Bad time format: {}".format(inputText)) # > 3.0
        
def parseFloat(inputText):
    # 003.5 0.5 01.5 8.6 1000.56 100.
    reg=re.compile(r"^[+-]?(\d|[1-9]\d+)\.\d*$") 
    mo=reg.search(inputText)
    if mo:
        return float(mo[0]) # <=> return float(mo.group(0))
    else:
        raise ParseFloatError("Bad float format: %s" % (inputText))
    
if __name__ == "__main__":
    
    dateStr=("22/12/1903", "15/08/16", "45/08/16","15/08/016", "5/08/16")
    for d in dateStr:
        try:
            nd=parseDate(d)
            print(f"Parsing of {d} OK -> {nd}")
        except ParseDateError as ex:
            print(f"Bad format: {ex}")
           
    timeStr=("12:23", "13:45:56", "23h45","23H45M56", "45:67", "12;34")
    for t in timeStr:
        try:
            nt=parseTime(t)
            print(f"Parsing of {t} OK -> {nt}")
        except:
            print(f"{t}: bad format!!!", t)
                
    floatStr=("1244.456", "-3.56", "0.003","12", "003.4", "12;34")
    for f in floatStr:
        try:
            nf=parseFloat(f)
            print(f"Parsing of {f} OK -> {nf}")
        except Exception as ex:
            print(f"exception message: {ex}")
   