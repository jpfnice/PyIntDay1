import re



"""
{min,max}: between min and max occurences of the preceding character
{n,}: n or more occurences of the preceding character
+ <=> {1,}: one or more occurences
* <=> {0,}: zero or more occurences

$: the end of the string
^: the beginning of the string
.: any character except the new line

\d: a digit
\D: any character except a digit
\s: a "space"
\S: any character except a space
\w: an alphanumeric character
\W: any character except an alphanumeric character

Classes of characters:
    
[2468]: either 2 or 4 or 6 or 8
[23456] <=> [2-6]: either 2 or 3 or 4 or 5 or 6
[^a-ZA-Z]: any character except a character in this "class": a-ZA-Z

Note: 
    [0-9] <=> \d and [^0-9] <=> \D

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

# text="nUmBer is 200" 
# regexp=re.compile(r"^number", re.IGNORECASE) # a "raw" string

# text="nUmBer is 3457" 
# regexp=re.compile(r"\d\d\d") # 3 digits

#text="nUmBer is 37" 
#regexp=re.compile(r"\d{3}") # 3 digits

# text="nUmBer is 3788" 
# regexp=re.compile(r"\d{3,6}") # between 3 and 6 digits

# text="nUmBer is 37" 
# regexp=re.compile(r"\d{3,}") # 3 or more digits

# text="nUmBer is 356" 
# regexp=re.compile(r"\d+") # + <=> {1,} 1 or more digits
#                           # * <=> {0,} 0 or more digits
#                           # ? <=> {0,1} 0 or 1 digits

# text="nUmBer is -356" 
# regexp=re.compile(r"[+-]\d+") # + or - followed by 1 or more digits

# text="nUmBer is 356" 
# regexp=re.compile(r"[+-]?\d+") # an optional + or - followed by 1 or more digits

# text="nUmBer is -356" 
# regexp=re.compile(r"123") # the sequence of digits 123
# regexp=re.compile(r"[123]") # the digit 1 or the digit 2 or the digit 3
# regexp=re.compile(r"[1-3]") # the digit 1 or the digit 2 or the digit 3

# text=": Some textual information" 
# regexp=re.compile(r"^[234TRYghu,:]") 

# text=";nUmBer is -356" 
# regexp=re.compile(r"^[^A-Za-z]") # any character except an alphabetic character at the begining of the string

text=";;;" 
regexp=re.compile(r"^...$") # the string is composed of 3 characters

if regexp.search(text):
    print("The string text 'match'")
else:
    print("The string text does not 'match'")
    
    
    
    
    
    
