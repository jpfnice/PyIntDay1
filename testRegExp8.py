import re

text="+8977654 the end"


regexp=re.compile(r"[+-]?\d+")

if regexp.match(text):
    print("The string text 'match'")
else:
    print("The string text does not 'match'")
