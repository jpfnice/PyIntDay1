import re

text="equip1: 234  equip2: 567  equip3: 890 equip4: 236"

"""
findall()
\b      means: "word boundary"

"""

regexp=re.compile(r"\b\d+\b")

# ob=regexp.search(text)
# print(ob.group(0))

for e in regexp.findall(text): # To get each number in turn
    print(e)

# listNumbers=regexp.findall(text)
# print(listNumbers)

#regexp=re.compile(r"equip\d")

#regexp=re.compile(r"e[^:]+")

# ob=regexp.search(text)
# print(ob.group(0))

# for e in regexp.findall(text): # To get each number in turn
#     print(e)