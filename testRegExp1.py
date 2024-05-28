import re

text="value:   899" # text="number:   899"

"""
{min,max}: between min and max occurences of the preceding character
{1,}: one or more occurences
+ <=> {1,}: one or more occurences
* <=> {0,}: zero or more occurences

$: the end of the string
^: the beginning of the string

\d: a digit
\D: any character except a digit
\s: a "space"
\S: any character except a space
\w <=> [a-zA-Z0-9]: an alphanumeric character
\W: any character except an alphanumeric character

[2468]: either 2 or 4 or 6 or 8
[23456] <=> [2-6]: either 2 or 3 or 4 or 5 or 6
[^a-ZA-Z]: any character except an character in this category: a-ZA-Z

(word1|word2|...): either "word1" or "word2" or ...
"""
#regexp=re.compile(r"\d\d\d") # a raw string
#regexp=re.compile(r"\d{3,5}") # a raw string
#regexp=re.compile(r"^\d{3,5}$") # a raw string
#regexp=re.compile(r"^\d{3,5}") # a raw string
#regexp=re.compile(r"^\d{3,5}$") # a raw string
#regexp=re.compile(r"^\d{3,5}\s+\d{3,5}$") # a raw string
#regexp=re.compile(r"^[2468]+\s+\d{3,5}$") # a raw string
#regexp=re.compile(r"^[a-z]+\s+\d{3,5}$") # a raw string
#regexp=re.compile(r"^[a-zA-Z]+\s+\d{3,5}$") # a raw string
#regexp=re.compile(r"^[^a-zA-Z]+\s+\d{3,5}$") # a raw string
regexp=re.compile(r"^(value|number):") # a raw string

if regexp.search(text):
    print("The string text 'match'")
else:
    print("The string text does not 'match'")
    
    
    
    
    
    
