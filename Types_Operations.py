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
print(line.rstrip())            # outputs aas,ssdad,EHE,SDsd,dSD,SD,dSDWFGWETHsdsd
                                # removes the right side spaces



