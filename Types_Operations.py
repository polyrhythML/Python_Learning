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
