import re

text="123 56:678   789;;897"

"""
the method sub()
"""

print("Original text:", text)

regexp=re.compile(r"[;:\s]+")


result=regexp.sub(",", text)

print("Text after substitution:", result)

# text=text.replace(" ",":")
# print(text)