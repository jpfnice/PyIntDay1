import re

text="begin 678   876 end"

# regexp=re.compile(r"(\d+)\s+(\d+)")
# matchobj=regexp.search(text) # A Match Object is returned
# if matchobj:
#     print("The string text 'match'")
#     print(matchobj.groups())
#     print(matchobj.group(0))
#     print(matchobj.group(1))
#     print(matchobj.group(2))
#     print(matchobj.group())

# else:
#     print("The string text does not 'match'")

regexp=re.compile(r"\d{2,3}")
matchobj=regexp.search(text) # A Match Object is returned
if matchobj:
    print("The string text 'match'")
    #print(matchobj.groups())
    print(matchobj.group(0))
    #print(matchobj.group())

else:
    print("The string text does not 'match'")