import re

text="+8977654"

"""
\d     a digit <=> [0123456789] <=> [0-9]
+      1 or more occurrences
{min,max} between [min,max] occurrences
{2,}    2 or more occurences
{3}     3 occurrences
{1,} <=> +
{0,} <=> *
{0,1} <=> ?
[abcAR65]
"""

regexp=re.compile(r"[+-]?\d+")

if regexp.match(text):
    print("The string text 'match'")
else:
    print("The string text does not 'match'")
