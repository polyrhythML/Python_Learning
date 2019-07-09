import math
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
