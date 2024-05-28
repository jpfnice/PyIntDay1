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

