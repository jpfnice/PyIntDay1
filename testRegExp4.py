import re

text="123 56:678   789;;897"

"""
sub()
"""

regexp=re.compile(r"[;:\s]+")


result=regexp.sub(",", text)

print(result)

# text=text.replace(" ",":")
# print(text)