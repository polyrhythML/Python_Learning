import math
import decimal
from fractions import Fraction
# Here we will look at some numeric types in python and their operations in python

# Integer -- > string of decimal digits
# Floating point number -- > decimal part + signed exponent
"""
Floating point number are implemented as C "doubles" in standard CPython and therefore get as much
precision as the C compiler used to build the Python interpreter gives to doubles
"""
# Integer types in Python
"""
2.X--->
* Normal 
* long
integer are automatically converted to long in case of the overflow

3.X--->
* both normal and long have been merged into a single type

Complex numbers --->
real part + imaginary part(j)
Internally, complex numbers are implemented as pairs of floating point numbers 
"""

# print(3.14  + "abc")     error

# Comparison Chained and Normal
X = 2
Y = 3
Z = 5
# Normal
if (X > Y) and (Y < Z):
    print("this is normal comparison")
# Chained
if X > Y > Z:
    print("this is chained comparison")
"""
Note : 1==2>3 ----> 1==2 and 2>3 
which is not equivalent to False<3 which means 0 < 3 i.e. true
"""


"""
DIVISION : CLASSIC , FLOOR , AND TRUE 
"""
# 3.X
print(10/4)     # True Division : outputs 2.5
print(10/4.0)   # True Division : outputs 2.5
print(10//4)    # Floor Division : outputs 2
print(10//4.0)  # Floor Division : outputs 2.0

# 2.X
print(10/4)     # Classic Division : outputs 2
print(10/4.0)   # Classic Division : outputs 2.5
print(10//4)    # Floor Division : outputs 2
print(10//4.0)  # Floor Division : outputs 2.0

# Note : X = Y /float(Z) -- > guarantees an output of float either in 2.X or 3.X

"""
FLOOR VS TRUNCATION
"""

print(math.floor(2.5))      # outputs : 2
print(math.floor(-2.5))     # outputs : -3 floors it to the nearest smallest
print(math.trunc(2.5))      # outputs : 2
print(math.trunc(-2.5))     # outputs : -2 truncates trims closer to the zero

"""
BINARY , HEXAL , OCTAL , DECIMAL REPRESENTATIONS IN PYTHON
"""

# Python can be coded in hex, octal , decimal and binary notations
# As we all know , Binary - 0,1
# Octal literal - 0-7
# Hexa literal - 0-9/A-F

# base/Radix - number of digits / combination of digits used to represent counting of masses
# let's try to represent some decimal numbers into hexadecimal , octal and binary

print("This is binary babes : {}".format(bin(64)))          # outputs : 0b1000000
print("This is hexadecimal babes : {}".format(hex(64)))     # outputs : 0x40
print("This is octal babes : {}".format(oct(64)))           # outputs : 0o100
print("{0:o}, {1:x}, {2:b}".format(64, 64, 64))             # same output as above , just with string formatting

# For fixed precision of your numbers you can use decimal module
print(decimal.Decimal(1)/decimal.Decimal(7))    # outputs : 0.1428571428571428571428571429
decimal.getcontext().prec = 4  # sets the number of digits of the precision
print(decimal.Decimal(1)/decimal.Decimal(7))    # outputs : 0.1429

# We have another module in our bag for floating point inaccuracies

x = Fraction(1, 3)
y = Fraction(4, 6)
print(x)                    # outputs : 1/3
print(y)                    # outputs : 4/6
print(Fraction("0.25"))     # outputs : 1/4
print(2.5.as_integer_ratio())         # outputs : (5, 2)

# Remember some conversions :
# fraction + int = fraction
# fraction + float = float
# fraction + float = float
# fraction + fraction = fraction

"""
Note : Sometimes you loss precision and its unavoidable , the numbers can be inaccurate in its original floating 
point form.
"""

print(4.0/3)                        # outputs : 1.3333333333333333
print((4.0/3).as_integer_ratio())   # outputs : (6004799503160661, 4503599627370496)


"""
TIME FOR SOME SETS : 
unordered collection of the immutable objects that support operations corresponding to the set theory
"""

x = set("abcde")
y = set("bdxyz")
print(x)            # outputs : {'a', 'c', 'd', 'b'}
print(y)            # outputs : {'d', 'x', 'b', 'z', 'y'}

print(x - y)        # outputs the difference(present in x) : {'a', 'e', 'c'}
print(y - x)        # outputs the difference(present in y) : {'y', 'x', 'z'}
print(x | y)        # outputs the union : {'a', 'x', 'd', 'y', 'z', 'b', 'e', 'c'}
print(x & y)        # outputs the intersection : {'b', 'd'}
print(x ^ y)        # outputs symmetric difference : {'y', 'x', 'z', 'a', 'e', 'c'}
print(x > y)        # Check for superset
print(x < y)        # Check for subset
print('e' in x)     # Membership test
print(x.intersection(y))    # same as x & y

z = set(['b', 'd'])
print(z)            # outputs : {'d', 'b'}
z.remove("b")
print(z)            # outputs : {'d'}
z.update(set(["X", "Z"]))
print(z)            # outputs : {'d', 'Z', 'X'}

# sets dont support indexing and slicing
"""
Note : empty {} , still creates dict and to create a set , we need to use set()
s = {} creates a dict 
s = set() creates a set 

Sets can only contain immutable objects. Therefore, lists and dictionaries cannot be embedded in sets
"""
s = set()
print(s.add([1,1]))     # TypeError: unhashable type: 'list'
s.add((1,1))            # Adding tuple is fine since it is immutable
print(s)                # outputs : {(1,1)}

r = frozenset((1,2,3))  # As frozen as the ice beyond the wall
r.update((1,34,12))     # frozen set doesnot have update method
r.remove(1,2)           # frozen set doesnot have remove
print(r)                  # frozenset({1, 2, 3})

# Set comprehensions

s_comp = {x**2 for x in [1,2,3,4]}
print(s_comp)             # outputs : {16, 1, 4, 9}

# To make changes to the set , convert them into list and then do inplace chanages
c = list(set(r))
c.append(7)
print(c)                  # outputs : [1, 2, 3, 7]

# Differences in the comparison of lists an sets

L1 = [1, 3, 2, 4, 6, 5]
L2 = [1, 2, 3, 4, 5, 6]
print(L1 == L2)
print(set(L1) == set(L2))
print(sorted(L1) == sorted(L2))

"""
Note : Sets are useful in filtering out or finding intersections within large datasets
based on  a certain criteria....
"""
