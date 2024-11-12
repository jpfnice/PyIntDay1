import re

text="123;56:678;789   897:::89;100"

"""
the split() method
"""

regexp=re.compile(r"[;:\s]+") # The separator used to split the text is a 
        # sequence of 1 or more of theses characters: ; : or spaces

result=regexp.split(text)# split() method of regexp objects

print(result)

# First way to convert a list of str into a list of int:
newList=[]
for e in result:
    newList.append(int(e))

print(newList)

# Second way to convert a list of str into a list of int:
newList=[int(e) for e in result] # list comprehension shortcut
print(newList)

# Third way to convert a list of str into a list of int:
newList=list(map(int, result))
print(newList)

print(sum(newList))

   