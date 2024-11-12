import re

text="a number: 678 the end"



regexp=re.compile(r"\d+")
matchobj=regexp.search(text) # A Match Object is returned
if matchobj:
    print("The string text 'match'")
    #print(matchobj.groups())
    print(matchobj.group(0))
    print(matchobj.group())

else:
    print("The string text does not 'match'")