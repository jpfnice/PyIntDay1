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

# Test 1:
    
# text="This is a remark"

# regexp=re.compile("rem")

# if regexp.search(text):
#     print("The string match !")
# else:
#     print("The string does not match !")

# Test 2:
    
# text="remark number 1"

# regexp=re.compile("^rem")

# if regexp.search(text):
#     print("The string match !")
# else:
#     print("The string does not match !")

# Test 3:
    
# text="Bla bla rem"

# regexp=re.compile("rem$")

# if regexp.search(text):
#     print("The string match !")
# else:
#     print("The string does not match !")

# Test 4:
    
# text="rem"

# regexp=re.compile("^rem$")

# if regexp.search(text):
#     print("The string match !")
# else:
#     print("The string does not match !")

# Test 5:
# \d -> a digit 

# text="The value is 678"

# regexp=re.compile(r"\d$")

# if regexp.search(text):
#     print("The string match !")
# else:
#     print("The string does not match !")
    
# Test 5:
# [2468] -> 2 or 4 or 6 or 8
# \d <=> [0123456789] <=> [0-9]

# text="The value is 677"

# regexp=re.compile(r"[2468]$")

# if regexp.search(text):
#     print("The string match !")
# else:
    # print("The string does not match !")    

# Test 6:
# [aAbB] -> a or A or b or B
# \w <=> [a-zA-Z0-9]

# text="An example"

# regexp=re.compile(r"^[aAbB]")

# if regexp.search(text):
#     print("The string match !")
# else:
#     print("The string does not match !") 

# Test 7:
# [^0-9] -> any character except a digit
# [^0-9] <=> \D

# text="An example"

# regexp=re.compile(r"^\D")

# if regexp.search(text):
#     print("The string match !")
# else:
#     print("The string does not match !")
    
# Test 8:
# + -> 1 or more occurence
# * -> 0 or more occurence
# ? -> 0 or 1 occurence

# text="word1     word2"

# regexp=re.compile(r"^\w+\s+\w+$")

# if regexp.search(text):
#     print("The string match !")
# else:
#     print("The string does not match !")
    
# Test 9:
# + -> 1 or more occurence
# * -> 0 or more occurence
# ? -> 0 or 1 occurence

# text="+56"

# regexp=re.compile(r"^[+-]?\d+$")

# if regexp.search(text):
#     print("The string match !")
# else:
#     print("The string does not match !")    
    
# Test 10:
# {1,3} -> 1, 2 or 3 occurences
# {5,} -> 5 occurences or more
# {3} -> 3 occurences
# * <=> {0,}, ? <=> {0,1}, + <=> {1,}

# text="+56"

# regexp=re.compile(r"^[+-]?\d+$")

# if regexp.search(text):
#     print("The string match !")
# else:
#     print("The string does not match !")       
    

# Test 10:
# . -> a character (except \n)

# text="+56"

# regexp=re.compile(r"^...$") # 3 characters

# if regexp.search(text):
#     print("The string match !")
# else:
#     print("The string does not match !")  
    
# Test 11:
# (value1|value2|value3 ...)

text="data.png"

regexp=re.compile(r"\.(gif|jpeg|png)$") # 3 possible suffixes: .gif, .jpeg or;png

if regexp.search(text):
    print("The string match !")
else:
    print("The string does not match !")
    

    
    
    
    
    
    
