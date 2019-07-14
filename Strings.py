# Lets Study some string operations in Python

## An ordered collection of characters used to store and represent text and bytes based information
## Python Strings are immutable

S = r"/temp/spam"       # Raw Strings
B = b"sp1xc4m "         # Byte Strings (Byte literal)
U = u"spluooc4m"        # unicode Strings (Unicode literal)

# So, unicode strings are not required to be decoded in any of the unicode formats

string1 = "PINEAPPLETHEIF"
string2 = "GAVINHARISSION"

# Some general String operations
print(string1 + string2)            # outputs : PINEAPPLETHEIFGAVINHARISSION
print(string1 * 2)                  # outputs : PINEAPPLETHEIFPINEAPPLETHEIF
print(string2 * 3)                  # outputs : GAVINHARISSIONGAVINHARISSIONGAVINHARISSION
print(string1[2])                   # outputs : N
print(string1[3:6])                 # outputs : EAP
print(len(string1))                 # outputs : 14

## FORMATTING

word = "my world  "
print(word)                                     # outputs : my world
print("a %s parrot" % word)                     # outputs : a my world   parrot
print("a {0} parrot".format(word))              # outputs : a my world   parrot
print(word.find("wo"))                          # 3
print("a {0} parrot".format(word.rstrip()))     # outputs : a my world parrot (observe the spaces are gone from right
                                                # of the word

print(word.replace("my", "xx"))                 # outputs : xx world
print(word.split(","))                          # ['my world  '](create a list by splitting the list with that string ,)
print(word.isdigit())                           # outputs : FALSE , Checks up whether , word is digit or not
print(word.upper())                             # outputs : MY WORLD
print(word.endswith("d"))                       # outputs : FALSE

"""
SINGLE VS DOUBLE QUOTES ARE SAME !! 
Let's get the story right 
"""

# The reason for supporting both is that it allows you to embed a quote character of the other variety inside a string
# without escaping it with a backlash
print("knight's")                               # outputs : knight's
print('knight"s')                               # outputs : knight"s

# We can also embed quoted in the string by escaping them with backslash
print('knight\'s')

# Using Escape sequences
# They let us embed characters in strings that cannot be easily typed as a string
s = "a\nb\tc"       # \n and \t are escape sequence characters here
print(s)            # a
                    # b     c

# Some extra knowledge on unicodes
"""
Code point - a value given to a particular character in unicode 
Code plane - is like an axis or dimension for similar kind of values 
There are about 17 planes 
eg U+1D360, 1 is the code plane and D360 is the code for a particular value
"""






