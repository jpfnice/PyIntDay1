import re

text="filename=data.content.txt"

"""

{3}     3 occurrences

{0,1} <=> ?


"""


regexp=re.compile(r"^filename$")
matchobj=regexp.search(text)
if matchobj:
    print("The string text 'match'")
    print(matchobj.groups())
    print(matchobj.group(0))

else:
    print("The string text does not 'match'")