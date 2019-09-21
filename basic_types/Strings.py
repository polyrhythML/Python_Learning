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

# Byte objects - Sequences of bytes
# String object - Sequence of characters
# Bytes are machine readable

# For \ character in the string use \\ or use r""
print(r"\trippycode")           # outputs :\trippycode
print("\\trippycode")           # outputs : \trippycode

"""
Note : A string cannot end with a single backlash because the backlash escapes the 
following quote characters, to embed it in the string.

"""
#print(r"amitnssdinasdo\")           # SyntaxError: EOL while scanning string literal
# or
#print("amitnssdinasdo\")            # SyntaxError: EOL while scanning string literal
# If you want to have a string \ at the end of a raw string, you can do the following
a = r"amitsingh\\"
b = a[:-1]
print(b)

# Iterating over a Sting

string = "trippycode"

for i in string :
    print(i)

# Outputs :
# t
# r
# i
# p
# p
# y
# c
# o
# d
# e

print(i in string)  # memebership test   # Returns True
print("am" in "amrickskdonamndan")       # Substring search     # Returns True

# Indexing and slicing
#  t   r  i  p  p  y  c  o  d  e
#  0   1  2  3  4  5  6  7  8  9
# -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
print(string[0])            # outputs : t
print(string[1:3])          # outputs : ri
print(string[:])            # outputs : trippycode
print(string[-2:-1])        # outputs : d
print(string[:-1])          # outputs : trippycod
print(string[-3:])          # outputs : ode
print(string[2:6:2])        # outputs : ipc
print(string[1::3])         # outputs : rpo
print(string[-6:-3:2])      # outputs : pc
print(string[-6:3:-2])      # outputs : p
print(string[2:-10:1])      # outputs :
print(string[2:-10:-2])     # outputs : i

# Binary value to Character conversion in python
print(ord('s'))             # outputs : 115
print(chr(115))             # outputs : s

# Strings are immutable
# inplace changes cannot be made
# need to use string.replace method or we can concatenate the string


"""
NOTE : Every operation that yields a new string value , string methods generate new strings objects.
If you want to retain those objects, you can assign them to variable names 
Generating a new string object for each string, but this is not in efficient as python garbage collects
unreferenced string objects. 
"""

### STRING METHODS

# Methods that are attribute attached to the object that happens to reference to the callable functions
# Always have an implied subject
# Attribute fetch and Call  expression
# Below example examples it better

a = "trippycode"
print(a.find("co"))            # Here find- is the attribute to fetch
                                    # calling the find("co") is the callable expression

# Also , its better to note that string.replace("co", "d") created a new string
# Let's check
b = a.replace("co", "d")
print(b is a)              # False
print(b == a)              # False

"""
Performance improvement with string objects : 
If you want to get better performance over a string of larger size where you are performing operations over it,
better to convert the string into a type which has inplace operations, because otherwise each string operation 
leads to a new string object
"""
S = "sammy"
L = list(S)     # list is mutable type , therefor inplace changes
print(L)        # outputs : ["s", "a", "m", "m", "y"]

# to get back the string
back = "".join(L)       # Sammy is back
print(back)             # outputs : sammy

# Joining Substrings works faster compared to concatenating substrings individually

# STRING FORMATTING

print("%d %s %g you"%(1, "spam", 4.0))              # Outputs : 1 spam 4 you
print("%d %s %s you"%(1, "spam", 4.0))              # Outputs : 1 spam 4.0 you

# Basically, in the above expression every variabe is converted into a string

# Some String formatting for floating point numbers
x = 1.23452452495563
print("%e | %f | %g"%(x, x, x))         # outputs : 1.234525e+00 | 1.234525 | 1.23452
# %e - scientific notation
# %f - floating point notation
# %g - real number notation

print("%.2f"%(x))                       # Outputs : 1.23 decimal places number

# Dictionary based Formatting
print("%(qty)d more %(food)s"%{"qty": 1, "food" : "spam"})     # outputs : 1 more spam

# Some more string formattings

#print("{0:.f}, {1:.2f}, {2:06.2f}".format(x, x, x))

print("{0:X}, {1:o}, {2:b}".format(255, 255, 255))          # outputs : FF, 377, 11111111

















