import builtins
# Functions are used for maximizing the code reuse

# def creates an object and assigns it to a name
# def statements - generates a new function object
# lambda in-line function - return the object itself
# yield sends a result back to the caller , but remembers the state where it left from

# Generators use yield statements to send back a value and suspend their state such that they may be resumed later,
# to produce a series of results over time

# Some overview of the scopes
# Global - declares variables that are to be assigned at module level
# non local - variables in the enclosing function

# In Python, the caller and function share objects by reference, but there is no name aliasing.
# def is more like assignement itself
# def are not evaluated until they are reached and run, code inside defs is not evaluated until function's are reached
# function itself is an object , here

# Python will automatically detect the type mismatch and raise exception in the function call.
# We can do our own explicit test of the type mismatches , but we want flexibility in our code


def function(x, y):
    print(x * y)


function(2,3)                       # Outputs : 6
function("trippy", 2)               # Outputs : trippytrippy
#function ("trippy", "code")         # Outputs : TypeError: can't multiply sequence by non-int of type 'str'

# All local variable dissappears when function exits, the return statement at the end of intersect sends back the
# result object

# A function doesnot remember the variables betweent the calls, although object returned by the function lives on
# retaining other sort of state info

"""
SCOPES : 

* prevents name clashes 
* retains info b/w function calls 

Namespace : 
* When you create a variable name, python looks up into the namespace to check for clashes, if there are any
* When we talk about the search for a name's value in relation to code, the term scope refers to a namespacem i.e
location of a name's assignment in source code

* Names defined inside a def , local to def
* Name defined inside enclosing function non local to the nested function
* Name defined outside all the variable assgined outside all defs, it is global to the entire life
"""
X = 99
print("This is global X : {}".format(X))            # Outputs : 99

def abc ():
    X = 88
    print("This is local X : {}".format(X))


def bcd():
    global X        # Accessing global variable
    print("Time to access and change the global variable : {}".format(X))
    X = 100


abc()                   # Outputs : 88
bcd()                   # Outputs : 99
print(X)                # Outputs : 100


# Enclosing module is a global scope
"""
Global variables becomes attributes of a module object to the outside world after imports but can be used as simple 
variables within the module file itself
"""

L = [1,2,3]

# In-place changes to objects do not classify names as locals
def inplace_method():
    L.append(4)
    print(L)


inplace_method()                # Outputs : [1,2,3,4]
print(L)                        # Outputs : [1,2,3,4]

# NAME RESOLUTION : THE LEGB RULE
# local - > Enclosing -> global -> Built-in

# Comprehension variables local comprehension itself

a = [local for local in [2,3,4,6]]
#print(local)                        # Name Error : Local variable not defined


print(dir(builtins))
# All the below names are in builtin
"""
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWar
ning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'Deprecation
Warning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError
', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', '
IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADir
ectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'Pro
cessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopI
teration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalE
rror', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueErro
r', 'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__',
'__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classme
thod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter',
 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclas
s', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'prin
t', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super
', 'tuple', 'type', 'vars', 'zip']
"""

print(zip is builtins.zip)          # Outputs : True
#print(True is builtins.True)        # Gives Syntax error

#True is a reserved keyword, and that means you cannot use it as an attribute name either.
#Like names, attributes must be valid Python identifiers.

# GLOBAL AND NON LOCAL
# They are remotely like declarations in python
# They are name space declarations
# Global names must be declared only if they are unassigned within a function

y, z = 1, 2


def all_globals():
    global x
    x = y + z
    print(x)


all_globals()            # Outputs : 3
print(x)                 # Outputs : 3


# PROGRAM DESIGN : MINIMIZE GLOBAL VARIABLE USE

"""
Changing global variables can lead to well-known software problem because the variables values are dependent on the
order of calls to arbitrarily distant functions, programs can become difficult to debug

Globals generally make code difficult to understand and reuse than code consisting of self contained functions that
rely on locals
Multi-threading - do parallel processing in Python, also commonly depend on global variables,
they become shared memory b/w functions running in parallel threads and so act as a communication device.

"""

# Minimize Cross file Changes

X = 99 # First.py
# Second.py
#import first
#print(first.X)

"""
Once first.py imported, the second.py has access to all the variables of first.py, first.py 's namespace is 
morphed into the namespace of the second.py
The problem with first.X = 88 is for too implict , whosoever is charged with maintaining the code for first.X
has no clue that some arbitrarily far-removed module on the import chain can change x out from under him.

Such things leads to code inflexibility 
"""

# The way to do it

# first.py
#X  = 99
#def setx(new):               ----- > create a function which is visible and shows that you are calling it
#    global X                         to change the value of X
#    X = new

# Second.py
# import first
# first.setx(88)

def f1():
    X = 88
    def f2():
        print(X)
    return f2

action = f1()
action()                    # Outputs : 88

# Here e see f2 remember the scope of enclosing scope of X , even though f1 no more exists


# CLOSURE / FACTORY FUNCTION : remembering closing function's state is called closure or factory function
# Function objects remembers values in enclosing scopes regardless of whether these scopes are still present
# in memory of not
# In effect, they have attached packets of memory, which are local to each copy of the nested function created
# this is called "State retention"

# these factory functions are used to generated event handlers on the fly in response to the user's input that
# cannot be anticipated when the GUI is built.


def make(N):
    def action(M):
        return (M**N)
    return (action)


f = make(3)
output = f(2)
print(output)       # Outputs : 8
output = f(3)
print(output)       # Outputs : 27

# We see that make doesnot exits here after its call , but the value of the variable N persists in the
# enclosed function call action

p = make(2)
output = p(2)
print(output)       # Outputs : 4
output = p(3)
print(output)       # Outputs : 9


# Each factory function gets its own set of state information

# Closures can also be created when a class is nested in a def, the values of the enclosing function's local names
# are retained by reference within the class, or one of its mehtods

# PYTHONIC VIEW : FLAT IS BETTER THAN NESTED

def makeactions():
    acts = []
    for i in range(5):
        acts.append(lambda x : i**x)
    return acts
acts = makeactions()

print(acts[0](2))
print(acts[1](2))               # Above all give output as 16
print(acts[2](2))               # basically returing the last act call for each of the element
print(acts[4](2))


def makeactions():
    acts = []
    for i in range(5):
        acts.append(lambda x, i=i : i**x)       # this remembers the state of i
    return acts
acts = makeactions()
print(acts[0](2))               # Outputs : 0
print(acts[1](2))               # Outputs : 1
print(acts[2](2))               # Outputs : 4
print(acts[4](2))               # Outputs : 16

# Non local Statements
# Nested functions have read and write access to names in the enclosing function.
# This makes nested scope closure more useful, by providing changeable info.


def tester(start):
    state = start
    def nested(label):
        print(label, start)
    return nested

F = tester(0)
F("spam")                       # Outputs : spam 0


def tester(start):
    state = start
    def nested(label):
        print(label, state)
        state += 1
    return nested


F = tester(0)
#F("spam")                     # UnboundLocalError: local variable 'state' referenced before assignment

# nonlocal to rescue


def tester(start):
    state = start

    def nested(label):
        nonlocal state
        print(label, state)
        state += 1
    return nested


F = tester(0)
F("spam")                       # Outputs : spam 0
F("nextspam")                   # Outputs : nextspam 1   --- > retains the state


# Some subtleties
# non local names really must be previously assigned in an enclosing def's scope when a non local is evaluated,
# or else you will get an error

"""
def tester(start):

    def nested(label):
        nonlocal state
        print(label, state)     # Output : SyntaxError: no binding for nonlocal 'state' found
        state += 1              # Gives out error
    return nested
"""

# Though its not the case with global


def tester():

    def nested(label):
        global state
        state = 0
        print(label, state)     # Output : SyntaxError: no binding for nonlocal 'state' found
        state += 1              # Gives out error
    return nested

X = tester()
out = X("label")                # Outputs : label 0
print(state)                    # Outputs : 1    global state
# X.state    ------ > no state object associated with  X , It is not visible outside the function
# Non locals are not looked up in the module's global scope or builtin scope outside the def, even if they already
# exist

spam = 99

"""
def tester():

    def nested(label):
        nonlocal spam
        print(label)            # Output : SyntaxError: no binding for nonlocal 'state' found
        spam += 1               # Gives out error
    return nested
"""
# It expects the spam to exist and pick up the global spam variable
# But it gives error , as theere is no binding to the non local variable spam
# F = tester()
# out = F("label")                # Outputs : SyntaxError: no binding for nonlocal 'spam' found



"""
Why nonlocal? State Retention Options 

* State information retention becomes crucial in many programs
* While functions can return results, their local variables wont be able to retain other values that must live 
between the calls
* Non local allows multiple copies of changeable state to be retained in memory
"""

# States with globals
"""
* Firstly, it requires global declaration in both functions and is prone to name collision in global scope
(if there is state already there)
* A more subtle problem is that it only allows for a single shared copy of the state information in the module 
scope
"""


def tester (start):
    global state
    state = start

    def nested(label):
        global state
        print(label, state)
        state += 1
    return nested


F = tester(10)
G = F("trippy")                         # Outputs : trippy 10
G = F("again trippy")                   # Outputs : trippy 11
G = F("again again trippy")             # Outputs : trippy 12

X = tester(111)
X1 = X("exams")                         # Outputs : exams
X1 = X("exams_1")                       # Outputs : exams_1
X1 = X("exams_2")                       # Outputs : exams_2


# Replacing nonlocal with an attribute


def tester(start):
    def nested(label):
        print(label, nested.state)
        nested.state += 1
    nested.state = start
    return nested


X = tester(10)
X1 = X("label")                     # Outputs : label 10
print(X.state)                      # Outputs : label 11     # Can accesss state as an attribute of the X

# Above code relies on the fact that assignment to a name, when it increments nested.state, it is changing
# part of the object nested references, not the name itself

# GLOBALS, NONLOCALS, FUNCTIONS, CLASSES ALL OFFER STATE RETENTION OPTION
# GLOBAL - > single copy shared data
# nonlocal -> changed in 3.X
# Classes - > requires a bit of OOPs



