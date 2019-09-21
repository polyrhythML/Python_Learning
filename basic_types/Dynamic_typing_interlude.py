import copy
import sys
"""
Polymorphism is the essence of Python programming and its dynamic nature makes it very flexible
in terms of code generalization
"""
# Let's understand how variables are created
# In python you dont declare variables
# Variables are created when assigned

a = 3

# Above we create a int object with value = 3
# Create a variable if it doesnot exist
# Link the variable to the int object 3
# Basically the variable a becomes reference to the int object (pointer to the object)

"""
OBJECTS : 

Each object has two standard header fields
* A type designator : mark type of the object
* Reference counter : when it's ok to garbage collect objects in python 
"""

# Same variable name can be used to point to the different objects in the code

a = 5       # Now a is pointing to int object 5
a = "spam"  # Now a is pointing to a string literal
a = 1.23    # Now a is pointing to a floating point

# At a time, it can point to only a particular object...

"""
OBJECTS ARE GARBAGE COLLECTED : 

Whenever a name is assigned to a new object , the space held by prior object is reclaimed if it 
is not referenced by any name or object.
This is called garbage collection - reclamation of the objec's space.
Makes file easy for the python programmer.
No allocation or deallocation of the memory required......
"""

# CYCLIC REFERENCE
# Objects points to self or reference another object that does.
# Examples , classes
# By default, the cyclic reference is enabled, but this component can be disabled.
# Since the reference count for such objects never goes to zero , they must be treated in a different manner
# will get to that in some time


"""
SHARED REFERENCE 
"""

a = 2
b = a

# Above both a and b point to the same int object 2 , this is called shared reference

# 1 : Some ambigous cases

a = 3
b = a
a = "spam"
# Now a points to string object "spam" but b still points to 3

# 2 :

a = 3
b = a
a = a+2
# Now , you would say that value of the int object 3 changes to 5
# both a and b point to int object which has value 5
# WRRRRRONG ------ > a points to a new int object 5 and b still points to the same int object 3
# CAUSE ---- > ints are immutables and cannot be changed inplace

"""
LESSONS FOR LIFE : In python setting a variable to a new value doesnot alter the original object, 
but rather causes the variable to refer an entirely new object

BUT NOT THE CASE WITH MUTABLE OBJECTS (EG. LISTs in place changes )

"""

# SHARED REFERENCES AND INPLACE-CHANGES

L1 = [2, 3, 4]
L2 = L1         # L1 and L2 refer to the same list object

L1[0] = 24
print(L1)       #[24, 3, 4]
print(L2)       #[24, 3, 4]
# Both L1 and L2 still point to the same list object with in-place change

# USE COPY OF THE LIST (ESCAPE IN-PLACE CHANGES)

L2 = L1[:]      # Makes a copy of the list object L1 was referencing to

# Now L1 an L2 refer to 2 different list objects
L1[0] = 12

print(L1)       # outputs : [12, 3, 4]
print(L2)       # outputs : [24, 3, 4]

# Slicing technique wont work in the case of sets, dicts since they are not sequence

# We have copy module to rescue chill ...

X = {1 : "Amit ", 2 : "Antony"}

Y = copy.copy(X)        # SHALLOW COPY (get to this later)
X[3] = "Inspirit-iot"

print(X)                # {1: 'Amit ', 2: 'Antony', 3: 'Inspirit-iot'}
print(Y)                # {1: 'Amit ', 2: 'Antony'}

# LETS SEE HOW DEEP CAN COPY GET
lis1 = [1, 2, [3, 5, 6], 7]
lis2 = copy.copy(lis1)
lis3 = copy.deepcopy(lis1)

lis3[2][1] = 100
print("Original : ", lis1)      # Original :  [1, 2, [3, 5, 6], 7]
print("Shallow  :", lis2)       # Shallow  : [1, 2, [3, 5, 6], 7]
print("Deep     :", lis3)       # Deep     : [1, 2, [3, 100, 6], 7]

lis2[2][1] = 110
print("Original : ", lis1)      # Original :  [1, 2, [3, 110, 6], 7]
print("Shallow  :", lis2)       # Shallow  : [1, 2, [3, 110, 6], 7]
print("Deep     :", lis3)       # Deep     : [1, 2, [3, 100, 6], 7]

lis2[1] = 90
print("Original : ", lis1)      # Original :  [1, 2, [3, 110, 6], 7]
print("Shallow  :", lis2)       # Shallow  : [1, 90, [3, 110, 6], 7]
print("Deep     :", lis3)       # Deep     : [1, 2, [3, 100, 6], 7]

lis1[1] = 33
print("Original : ", lis1)      # Original :  [1, 33, [3, 110, 6], 7]
print("Shallow  :", lis2)       # Shallow  : [1, 90, [3, 110, 6], 7]
print("Deep     :", lis3)       # Deep     : [1, 2, [3, 100, 6], 7]


# SHARED REFERENCE EQUALITY ------------------------>

X1 = 42
X1 = "Shruberry"

# Just like girls, its difficult to get python's reclamation
# The int object 42 , stays in the cache
# Python uses small strings , and integers keeps them in cache for reuse
# Since there is a likely possibility that you might end up using it again

L1 = [1, 2, 3]
M = L1
print(L1 == M)          # TRUE
print(L1 is M)          # TRUE

# BUT

L1 = [1, 2, 3]
M = [1, 2, 3]

print(L1 == M)          # outputs : TRUE
print(L1 is M)          # outputs : FALSE Strong test to check whether two variables refer to same object or not

# Getting the number of references of an object in the current scope
print(sys.getrefcount(L1))      # outputs : 2








