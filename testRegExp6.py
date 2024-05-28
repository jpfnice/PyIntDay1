import re

text="file: image.GiF"

"""
flags
methods vs functions
"""


# regexp=re.compile(r"[a-z]+\.(gif|jpg|png)", re.IGNORECASE)
# # # regexp=re.compile(r"[a-z]+\.(gif|jpg|png)", re.I)

# result=regexp.search(text)

# if result:
#     print("OK")
# else:
#     print("Not an image file")

    
    

result=re.search(r"[a-z]+\.(gif|jpg|png)", text, re.IGNORECASE)

if result:
    print("OK")
else:
    print("Not an image file")
    
    
    