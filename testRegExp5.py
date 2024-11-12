import re

text="date1: 2002:23:02 date2: 2004:21:04"

"""
the method sub()
"""

regexp=re.compile(r"(\d{4}):(\d{2}):(\d{2})")

# result=regexp.sub(r"\2/\3/\1", text)

# print(result)


matchObj=regexp.search(text)
if matchObj:
    print(matchObj.groups())
    print(matchObj.group(0))
    print(matchObj.group(1))
    print(matchObj.group(2))
    print(matchObj.group(3))

   