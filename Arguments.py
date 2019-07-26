# Let's start with pythonic Arguments


def f(a):
    a = 99                  # This only changes variables local to the function
    print(a)

b = 88


def f1(a):
    a = 100
    print(a)


print(b)                    # Outputs : 88
f(b)                        # Outputs : 99
print(b)                    # Outputs : 88
f1(b)                       # Outputs : 100
print(b)                    # Outputs : 88

# Hence, we see the value of b is not changed, it is still 88
# Situation is a bit different when you pass mutable objects as the argument


def changes(a, b):
    a = 2                   # This change is local
    b[0] = "spam"           # This change will be shared across the passed object
    print(b)
X = 1
L = [1, 2, 4]

print(X)                    # Outputs : 1
print(L)                    # Outputs : [1, 2, 4]
changes(X, L)
print(X)                    # Outputs : 1
print(L)                    # Outputs : ["spam", 2, 4]      This object got changed

"""
Reason for such behaviour : because a is a local variable in function scope, the first assignment has no 
effect on the caller. It simply changes the local variable a to reference a completely different object and doesnot
change binding of X in the caller's scope

Above example is equivalent to : 
X = 1 
a = X 
a = 2 
print(a)---------> it points to a new int object
print(X)---------> it points to its own original 1 int object 

similarly, 

b = [1, 2, 3 ]
b = L 
b[0] = 'spam'
print(b)
print(L)
"""

X = 1
a = X
a = 2
print(a)#---------> it points to a new int object
print(X)#---------> it points to its own original 1 int object

b = [1, 2, 3 ]
print(b)            # Outputs : [1, 2, 3]
b = L
b[0] = 'spam'
print(b)            # Outputs : ['spam', 2, 3]
print(L)            # Outputs : ['spam', 2, 3]



# To avoid changes to the mutable object, pass a copy of the objects


def changes1(a, b):

    a = 2                   # This change is local
    b[0] = "xyz"            # This change will be shared across the passed object
    print(b)


changes1(X, b[:])           # Outputs : ['xyz', 2, 4]
print(b)                    # Outputs : ['spam', 2, 4]

# Also we can convert to mutable object to work with

# Changes1(X, tuple(b))

# Return can sent back multiple values too, by default as a tuple, but we can have any type returned
# In fact, python doesnot support what we call as "call by reference" argument passing, we can simulate it by
# returning tuples and assigning the results back to original arg named in the caller

def multiple(x, y):
    x = 2
    y = 3
    return x, y
X = 1
L = 2
X, L = multiple(X, L)
print(X, L)                 # this prints 2 3

# Arguments matching

# Positional Arguments : matched left to right
# Keywords Arguments : matched with the name of the argument
# Defaults for the optional arguments
# Var args : *args , *kwargs -- > positional and keyword

# func(*literable) ------> passed object should be an iterable and arguments recognised by position
# func(**kwargs)   ------> passed all keys/value pairs in the dict as individual keyword arg

"""
important : Ordering rule 

positional arg, keyword args, default args, args(*iterable), args(**dict)
Hence, **args must come at the last if present 
"""

# Python's internally carries out to match :

# 1 : Assign non-keyword arguments by position
# 2 : Assign keyword args by name
# 3 : Assign extra non-keyword arg to *tuple
# 4 : Assign extra keyword args to **name dictionary


def name1(a, b, c):
    print(a, b, c)

name1(1, 2, 3)          # Positional arguments


def name2(a=1, b=2, d=3):           # keyword arguments(order doesnot matter)
    print(a, b, d)


name2(a=10, d=15, b=12)            # Outputs : 10 12 15


def name3(a, b=10, c=12):           # a is required , b and c are optional
    print(a, b, c)


name3(11)                           # Outputs : 11 10 12

name3(120, c=13)                    # Outputs : 120 10 13

# The mutable objects passed in the def header retains its state across multiple calls of the function
# Therefore, it is better to peform the assignment inside the funciton to a new varible instead of making place
# Changes to the function


def mutable_func(X, L):
    L[0] += 1
    print(X, L)

X = 1
L = [1, 2, 4]

mutable_func(X,L)                   # Outputs : 1 [2, 2, 4]
mutable_func(X,L)                   # Outputs : 1 [3, 2, 4]
mutable_func(X,L)                   # Outputs : 1 [4, 2, 4]

X = 1
L = [1, 2, 4]


def better_mutable_func(X, L):
    M = L[:]                        # Pass a copy of the L
    M[0] +=1
    print(X, M)
better_mutable_func(X, L)           # Outputs : 1 [2, 2, 4]
better_mutable_func(X, L)           # Outputs : 1 [2, 2, 4]
better_mutable_func(X, L)           # Outputs : 1 [2, 2, 4]
better_mutable_func(X, L)           # Outputs : 1 [1, 2, 4]

# So we see that here every call of the L gets the original copy of L and there is no change in the L
# in subsequent calls of the function compared to what we saw in the first case

# MUTABLE OBJECTS ALLOW STATE RETENTION----- BEWARE !!


def func_1(**args):
    print(args)

func_1(a=1, b=2)                   # Outputs : {'a' : 1, 'b' : 2}


def func_2(x, *args, **kargs):
    print(x, args, kargs)


func_2(1, 12, 34, 56, a=12, b=13)   # Outputs : 1 (12, 34, 56) {'a':12, 'b':13}


def func_3(a, b, c, d):
    print(a, b, c, d)

args = (1, 2)
args += (3, 4)
func_3(*args)                               # Outputs : 1 2 3 4

args = {'a': 1, 'b': 2, 'c': 3}
args.update({"d": 4})

func_3(**args)                              # Outputs : 1 2 3 4

func_3(*(1, 2), **({'c': 3, 'd': 4}))       # Outputs : 1 2 3 4

func_3(1, *(2, 3), **({'d':4}) )            # Outputs : 1 2 3 4

func_3(1, c = 3, *(2,), **({'d': 4}))       # Outputs : 1 2 3 4

func_3(1, 2, c = 3, **{'d': 4})             # Outputs : 1 2 3 4


# Note some corner cases for keyword argument

def func_4(a, *, b, c):
    print(a, b, c)

# The above function expects only 1 positional argument and 2 keyword argument Hence
# By running the below function call you will get an error

#func_4(1, 2, 3)         #TypeError: func_4() takes 1 positional argument but 3 were given


func_4(1, c=3, b = 2)    # Outputs : 1 2 3

# Here a has to be positional but b and c are not necessary, if sent, they must be keywords


def func_5(a, *, b = 2, c = 3):
    print(a, b, c)

# a has to be positonal, b has to be keyword and must be sent, c is optional but must be keyword
def func_6(a, *, b, c = 3):
    print(a, b, c)

"""
Note : Keyword args to be only coded before **args and after *args, when they are present
"""

#def func_7(a, *b, **d, c=6):   -------------> This gives syntax error
#    print(a, b, c, d)


def func_8(a, *b, c= 6, **d):
    print(a, b, c, d)

func_8(1,2,3,**{'d':4})             # Outputs : 1 (2,3) 6 {'d': 4}

# WHY KEYOWORD ONLY ARGS ???

"""
* makes it easier for allow a function to accept both any numbers of positional arguments to be processed
and config operations passed as argument
* Without the keywords only args, extra work may be required to provide defaults for such an option and to verify
that no superfluous keywords were passed
* Without variable args, you might have to either list all the possible options by position or hope for a judicious
positional argument default protocols that would handle every possible arrangements

"""









