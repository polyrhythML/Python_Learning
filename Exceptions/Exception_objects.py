# Why class based exceptions?

"""
• Can be organized into categories. Exceptions coded as classes support future
changes by providing categories—adding new exceptions in the future won’t generally
require changes in try statements.

• Have state information and behavior. Exception classes provide a natural place
for us to store context information and tools for use in the try handler—instances
have access to both attached state information and callable methods.

• Support inheritance. Class-based exceptions can participate in inheritance hierarchies to obtain and customize common behavior—inherited display methods,
for example, can provide a common look and feel for error messages.

"""

# Older way to define exceptions
"""
myexc = "This is pretty old"
try:
    raise myexc
except myexc:
    print("Caught")
"""


# Class-Based Exceptions
"""
Detailed difference : 

* When a try statement’s except clause lists a superclass, it catches instances of
that superclass, as well as instances of all its subclasses lower in the class tree. The net
effect is that class exceptions naturally support the construction of exception hierarchies: 
superclasses become category names, and subclasses become specific kinds of exceptions 
within a category. By naming a general exception superclass, an except
clause can catch an entire category of exceptions—any more specific subclass will
match.
* String exceptions had no such concept: because they were matched by simple object
identity, there was no direct way to organize exceptions into more flexible categories
or groups. The net result was that exception handlers were coupled with exception sets
in a way that made changes difficult.
"""


class General(Exception): pass
class Specific1(General): pass
class Specific2(General): pass


def raiser0():
    X = General()
    raise X


def raiser1():
    X = Specific1()
    raise X


def raiser2():
    X = Specific2()
    raise X


for func in (raiser0, raiser1, raiser2):
    try:
        func()
    except General:
        import sys
        print("Caught : %s"%sys.exc_info()[0])


# Why Exception hierarchies?
"""
For large or high exception hierarchies, however, it may be easier to catch 
categories using class-based categories than to list every member of a category 
in a single except clause. Perhaps more importantly, you can extend exception hierarchies as software needs evolve by
adding new subclasses without breaking existing code.

Naive way to code exceptions in your project/ library 

Example: 
You code a numeric programming library in Python, to be used by a large number of people. While you are writing your library, you identify two things
that can go wrong with numbers in your code—division by zero, and numeric overflow.

class Divzero(Exception) : pass
class oflow(Exception) : pass

def func():
...
raise Divzero()
...and so on...

# client.py 

import mathlib
try:
mathlib.func(...)
except (mathlib.Divzero, mathlib.Oflow):
...handle and recover...


* Now you find out about a new exception that needs to be handled by your code. You write 
another class to handle it.

# mathlib.py
class Divzero(Exception): pass
class Oflow(Exception): pass
class Uflow(Exception): pass

* You need to add that in every script in which you call that library funciton.
Not a good code design to follow.
# client.py
try:
mathlib.func(...)
except (mathlib.Divzero, mathlib.Oflow, mathlib.Uflow):
...handle and recover...

########### BETTER WAY TO CODE ################
Add subclass to the base class NumErr, this way the exception handling of the base class is
done with a class tree hierarchy where it finds the subclass handling that exception.

# mathlib.py
class NumErr(Exception): pass
class Divzero(NumErr): pass
class Oflow(NumErr): pass
def func():
...
raise DivZero()
...and so on...

# client.py
import mathlib
try:
mathlib.func(...)
except mathlib.NumErr:
...report and recover...

"""


# Built-in Exception Classes

"""
* BaseException: topmost root, printing and constructor defaults
The top-level root superclass of exceptions. This class is not supposed to be directly
inherited by user-defined classes (use Exception instead). It provides default print-
ing and state retention behavior inherited by subclasses. If the str built-in is called
on an instance of this class (e.g., by print ), the class returns the display strings of
the constructor arguments passed when the instance was created (or an empty
string if there were no arguments). In addition, unless subclasses replace this class’s
constructor, all of the arguments passed to this class at instance construction time
are stored in its args attribute as a tuple.

* Exception : root of user-defined exceptions
The top-level root superclass of application-related exceptions. This is an imme-
diate subclass of BaseException and is a superclass to every other built-in exception,
except the system exit event classes ( SystemExit , KeyboardInterrupt , and Genera
torExit). Nearly all user-defined classes should inherit from this class, not BaseEx
ception . When this convention is followed, naming Exception in a try statement’s
handler ensures that your program will catch everything but system exit events,
which should normally be allowed to pass. In effect, Exception becomes a catchall
in try statements and is more accurate than an empty except.

* ArithmeticError : root of numeric errors
A subclass of Exception , and the superclass of all numeric errors. Its subclasses
identify specific numeric errors: OverflowError , ZeroDivisionError , and Floating
PointError.

* LookupError : root of indexing errors
A subclass of Exception , and the superclass category for indexing errors for both
sequences and mappings— IndexError and KeyError —as well as some Unicode
lookup errors.
"""

# use __str__ instead of __repr__ to customize exception handling log values

