from collections import namedtuple
# Let's Study a bit about tuples and files

# Tuples are immutables
# No inplace changes
# Usually written as the series of the items in paranthesis
# Share most of the properties with lists
# Fixed length , arbitrary nestable , heterogeneous
# Stores the references to other objects

T = ("amit", "1.3", 3)
T1 = ("Bob", ("dev", "mgr"))
T2 = tuple("spam")
print(T)                # Outputs : ('amit', '1.3', 3)
print(T1)               # Outputs : ('Bob', ('dev', 'mgr'))
print(T2)               # Outputs : ('s', 'p', 'a', 'm')

print(T*3)              # Outputs : ('amit', '1.3', 3, 'amit', '1.3', 3, 'amit', '1.3', 3)
print(T1[0])
print(T1[1:3])

x = (40)                # This is an integer object
x1 = (40,)               # This is tuple
x2 ="1" , "3" , "trippy", "xyz"
print(x)                # Outputs : 40
print(x1)               # Outputs : (40,)
print(x2)               # Outputs : ('1', '3', 'trippy', 'xyz')

# Python allows us to omit the paranthesis in the cases where it is not required or the cases where it
# becomes ambiguous to do so.

# list from the tuple
L1 = list(x2)
print(L1)               # Outputs : ['Bob', ('dev', 'mgr')]
L1.sort()
print(L1)               # Outputs : ['1', '3', 'trippy', 'xyz']
# You can get back the tuple
back = tuple(L1)
print(back)             # Outputs : ('1', '3', 'trippy', 'xyz')

"""
Note : Immutability of a tuple is applied only to the top level tuple itself, not to the elements inside it..
"""

T = (1, [2,3], 5)
# T[3]= 7                  Outputs : TypeError: 'tuple' object does not support item assignment
T[1][0] = 4
print(T)                # Outputs : (1, [4, 3], 5)

# WHY TUPLES
"""
Tuples are used bcos of the guarantee for not changing in any reference it. It has an integrity..
Lists dont guarantee that
"""

# WE have named tuples for key values using tuples
Rec = namedtuple("Rec", ["name", "age", "jobs"])
bob = Rec("Bob", age = 40, jobs = ["dev", "mgr"])

print(bob)                # Outputs : Rec(name='Bob', age=40, jobs=['dev', 'mgr'])
print(bob[0])             # Outputs : bob
print(bob[1])             # Outputs : 40

# FILES

"""
Builtin open functions creates a python file object, which serves as a link to a file residing on your machine.
Transfer strings of data to and from associated external file by calling the returned file object's methods
"""
# how to open and close a file....
afile = open("xyz.txt", mode="r")
afile.close()

"""
Filenames may contains non-ASCII unicode characters that python translates automatically from the underlying
platform encoding....

* file iterator are best for reading lines
* Content is String and not Objects
* Files are buffered and seekable
* use context managers to automatically close the file scope automatically onece you have used it 

"""

# Text and binary files

"""
* Text files represent content as normal strings perfomr unicode encoding and decoding automatically, and performs
end-of-line translation by default.
* Binary files represent content as a special bytes string type and allow program to access file content un-altered

Python 3.X - all kinds of text have been merged in the normal string types - which makes sense, given that all text
is unicode, including ASCII and other 8 bit-encodings
"""

# SHARED REFERENCES EXAMPLES

X = [1, 2, 3]
L = ["a", X, "b"]
D = {"x": X, "y": 2}
print(L)                # Outputs : ['a', [1, 2, 3], 'b']
print(D)                # Outputs : {'x': [1, 2, 3], 'y': 2}

# copying the X and not refering to the origin X
L1 = ["a", X[:], "b"]
D1 = {"x": X[:], "y": 2}
print(L1)                   # Outputs : ['a', [1, 2, 3], 'b']
print(D1)                   # Outputs : {'x': [1, 2, 3], 'y': 2}
print(L[1] is L1[1])        # Outputs : False
print(D["x"] is D1["x"])    # Outputs : False

# TRUE AND FALSE IN PYTHON
# Non zero numbers are True and zero is a False

if -1:
    print("Negatives are also True")            # Outputs : Negatives are also True
if L1 :
    print("Even list objects are True")         # Outputs : Even list objects are True
L1 = []

if not (L1) :
    print("Empty object are False")             # Outputs : Empty objects are False
L1 = None
if not(L1) :
    print("None is also false")                 # Outputs : None objects are also false

# Bool type prints out true or false in place of 1 pr zero

print(bool({}))                                 # Outputs : False
print(bool("sapm"))                             # Outputs : sapm
print(bool(None))                               # Outputs : False









