# Assignments create Object references
# They create reference to objects instead of copying them back
# Python variables are more like pointers
# Names must be assigned before referencing
# Various assignment forms :
spam = "spam"                       # Basic Form
spam, ham = "spam", "ham"           # Tuple Assignment
[spam, ham] = ["spam", "ham"]       # List Assignment
a, b, c, d = "spam"                 # Sequence sequence packing
a, *b = "spam"                      # Extended sequence packing
spam = ham = "lunch"                # Mulitple-target assignment
#spam +=42                           # Augumented assignment

# Swapping
#nudge, wink = wink, nudge

# Sequence assigment supports any iterable object on right

string = "SPAM"
# a, b, c = string  This gives error : Value Error too many values to unpack
a, b, c = string[0], string[1], string[2]
a, b, c = list(string[:2]) + [string[2:]]
print(a, b, c)                              # Outputs : ('S', 'P', 'A')
(a, b), c = string[:2], string[2:]          # Output : ('S', 'P', 'AM')
print((a, b), c)

# Nested sequence, Python unpacks their parts to their shape.
((a,b), c) = ('SP', 'AM')
print(a,b,c)                # Outputs : S P AM

print([(a, b, c) for (a, b, c) in [(1, 2, 3), (4, 5, 6)]])

# Extending unpacking
seq = [1, 2, 3, 4, 5, 6, 7]
*a, b = seq
print(a, b)                     # Outputs : [1, 2, 3, 4, 5, 6] 7
a, *b, c = seq
print(a, b, c)                  # Outputs : 1 [2, 3, 4, 5, 6] 7

a, b, *c = seq
print(a, b, c)                  # Outputs : 1 2 [3, 4, 5, 6, 7]

# Let's take some boundary cases

sequence = [1, 2, 3, 4]
a, b, c, *d = sequence
print(a, b, c, d)               # Outputs : 1 2 3 [4]
# If there is nothing to unpack, last element becomes empty list
a, b, c, d, *e = sequence
print(a, b, c, d, e)            # Outputs : 1 2 3 4 []

a, b, *e, c, d = [1, 2, 3, 4]
print(a, b, c, d, e)            # Outputs : 1 2 3 4 []


# a, b, e, c, d = [1, 2, 3, 4]
# print(a, b, e, c, d)           # Throws error not enough values to unpack(expected 5, got 4)

# a, *b, c, *d = seq             # Outputs : SyntaxError: two starred expressions in assignment

#*a = seq                         # Outputs : SyntaxError: starred assignment target must be in a list or tuple
print(a)

# Let's see some applications

print([(a, b, c) for (a, *b, c) in [(1,2,3,4), (3,4,5,6), (4,5,6,7), (4,7,8,9)] ])
# Outputs : [(1, [2, 3], 4), (3, [4, 5], 6), (4, [5, 6], 7), (4, [7, 8], 9)]

# Multiple target assignements
a = b = 1
a = a+1
print(a)        # Outputs : 2
print(b)        # Outputs : 1

# We see that initially a and b referred to the same object 1 but, the operation a = a + 1
# makes a reference a new object , and b still refers to the 1 int object

# Different case with mutable assignments
a = b = []
a.append(1)
print(a, b)                 # outputs : [1] [1]

# Hence we need to assign a and b to two different list objects
a, b = [] , []
a.append(1)
print(a, b)                 # Outputs : [1] []

# Augumented Assignment
a = 2
a = a +1        # Normal addition
a += 1          # Augumented assignment
# Optimal techique is automatically chosen.That is , for objects that support in-place changes, the augumented
# forms automatically perform in-place change operations instead of slower copies

L = [1, 3]
L = L + [2]     # Concatenate is Slower
L.append(2)     # append is faster
print(L)        # Outputs : [1, 3, 2, 2]

L += [5]        # Python automatically calls the quicker method to append the list

# Concatenation operations create a new object, copy in the list on the left and then on the right.
# By Contrast, in-place method calls simply adds items at the end of the memory.
# L = L + [3] and L += [5] are not the same

# Difference between concatenate and change in place
L = [1, 2]
M = L
L = L + [3,4]
print(L, M)                 # Outputs : [1, 2, 3, 4] [1, 2]

L = [1,2]
M = L
L += [3, 4]
print(L, M)                 # Outputs : [1, 2, 3, 4] [1, 2, 3, 4]

# Bit of naming conventions
# __x__ - > system defined names
# _x are not imported by from a module import * statement
# __x   - > begins with two underscores and do not end with two or more, are localized to enclosing classes


"""
Note : 
Objects have a type and maybe be mutable or not. Names, on the other-hand, are always just
references to objects, they have no notion of mutability and have no associated type information, 
apart from the type of the object they happen to reference at a given point in time.
"""

## PRINT OPERATIONS
# Syntax : print([object], [sep=""], [end=""], [file=""]])
# object - is th object to write with some formatting
# sep - is the separator between the objects
# end - is the character at the end of the line
# file - standard stream to which to write (stdin, stdout, stderr)

import sys
# Using standard output stream to write data
# This is more of an explicit method to write to the streams
temp = sys.stdout
sys.stdout.write("hello world")
# This redirects the print to this file
sys.stdout = open("./xyz.txt", "a")

# We can even redirect sys.stdout to an object than isnt a file at all, as long as it has the expected interface,
# a file as it has the expected interface, a method named write

print("I have directed my stdout stream to write to a file ") # This goes to the file , not here
print("Yup, i am writing in there")
sys.stdout.close() # Flush outputs to the disk
sys.stdout = temp
print("Print is back babes ")

# We can see that content of the file has the string from above print statements
file = open("./xyz.txt", mode="r")
print(file.readlines())
file.close()


# TRUTH VALUE AND BOOLEAN TEST
# All objects have an inherent Boolean true or false values
# Zero non-zero number or non-empty object is true
# Zero number, empty objects and special object None are false
# Comparison and equality returns true and false
# Boolean operator stops operating as soon as result is known (short circuit)

print(2 < 3, 3 < 2)             # Outputs : True False
print(2 or 3 , 3 or 2)      # Outputs : 2 3
print(2 and 3, 2 and 3)     # Outputs : 3 3

# If False , left is return, if True , right is returned

print({} and [])            # Outputs : {}
print({} and  1)            # Outputs : {}

X = [] or {} or () or 3 or None
print(X)                                # Outputs : 3
# Prints the first non zero element
# So, basically the point is or and add operators return the object
# Comparison and equality operator returns True or False
# With this we conclude our this script ... Ae dil kisi ki yaad mein hota hai bekarar kyun







