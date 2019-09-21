"""
In low level languages such as C, C++ , you know much of your work centers around on implementing objects,
Memory Management. Layering out memory structures, managing memory allocations , implement search and so on.
These are tedious and prone to error.
In python all these are mad easier by builtin functions to be used , which make it really simple for you to
the prime goal and code without being concerned about the under the hood complications
"""


# Strings

S = "spam"
print(len(S))       # outputs 4
print(S[0])         # outputs s
print(S[len(S)-1])  # outputs m
print(S[1:3])       # outputs pa
print(S[1:])        # outputs pam
print(S[:-1])       # outputs spa
print(S[:])         # outputs spam
print(S+"xyz")      # outputs spamxyz
print(S*4)          # outputs spamspamspamspam

# We see that S uses + as well as * in the string operations which is also used with integers
# This is called Polymorphism
# The operation type depends upon the type of the object itself.

"""
String are immutable types in python means cannot be changed inplace
after they are created or you can never overwrite the values of immutable objects.
"""
# Below operation cannot be performed
#S[0] = "z"
# error --> TypeError: 'str' object does not support item assignment

# Type Specific Methods :
print(S.find("pa"))             # outputs 1
print(S.replace("a", "bit"))    # outputs spbitm

line = "aas,ssdad,EHE,SDsd,dSD,SD,dSDWFGWETH"
print(line.split(","))          # outputs : ['aas', 'ssdad', 'EHE', 'SDsd', 'dSD', 'SD', 'dSDWFGWETH']
line = line + "sdsd   "
# Removes the right side spaces
print(line.rstrip())            # outputs aas,ssdad,EHE,SDsd,dSD,SD,dSDWFGWETHsdsd

# String Formatting

print("%s , eggs , and %s "%("spam", "SPAM"))
print("{0} , eggs , and {1} ".format("spam", "SPAM"))
print("{} , eggs , and {} ".format("spam", "SPAM"))
print("{:.2f}".format(296999.2567))

# Python 3.X strings are unicode encoded text
# print(u"X" + b"y")  # works in 2.X
print(u"X" + "y")   # works in 3.X , work as u"xy"

# Python 2.X types are objects and 3.X types are classes
# print(type(L))   <type "list">
# print(type(L))  # <class "type">

# There are 3 ways to check type of an object in python
L = []
if(type(L)) == type([]):
    print("yes")
elif type(L) == list:
    print("Check2")
elif isinstance(L, list):
    print("Check3")
else:
    print("I don't have any other way to check the types in the python")

