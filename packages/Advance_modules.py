# Module Design Concepts

"""
* You are always in a module  : There is no way to write code that doesnot live in a module. Even the interactive prompt
code you run is , written in a main module.

* Minimize the module coupling, global variables : As a rule of thumb, they should be independent of global variables
used within other modules as possible.

* If all the components of a module serve a general purpose, you are less likely to depend on external names.

* Modules should rarely change other modules variables : You should try to communicate results through devices such as
function arguments and return values, not cross module changes.

"""

# HIDING OBJECTS IN MODULES

"""
* one thing is you can put an underscore in front of the variables in a modules, so when you import it using from * 
you will not see that 
"""
from b import *

print(a)                # Outputs : 1
#print(_d)               # Outputs : NameError: name '_d' is not defined

"""
* Another convention to follow is using __all__ list variable in __init__.py

* You can explicitly define what variables to import from a module when importing it when using from x import * 

"""

# __name__ and __main__

"""
* This trick helps us run a python module as a main script as well as a import module

* Each module has a built in attribute called __name__, which Python creates and assigns automatically as follows : 
    
    * If the file is run as a top level file, the name attribute is set to __main__
    * If the file is being imported, the name attribute is set to the name of the module as imported by the clients.

if __name__ == "__main__ ":
    tester()
    
* This kind of technique is used for self package code testing. Testing your script whether it works fine or not....   
"""


# Let's take up an example to see how this works

def tester(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res


def lessthan(x, y):
    return x < y


def greaterthan(x, y):
    return x > y


#if __name__ == "__main__":
#    print(tester(lessthan, 4, 2, 3, 1, 5, 6))
#    print(tester(greaterthan, 2, 1, 4, 5, 3))


# You can also write a script and check with the sys.argv whether the first commandline argument is the name of the
# script itself...


# Changing the module Search Path

"""
* WE saw module's search path is added to the list of directories using PYTHONPATH environment variables. 
* We can changes the search path explicitly by accessing the attribute path of a module called sys.
"""
import sys
print(sys.path)

# once you make such an import, it will impact all future imports anywhere while a Python program runs, as all importers
# share the same single sys.path list


# How to get name of attributes of a moudle

#sys.modules["M"].name
#getattr(M, name)
#M.__dict__["name"]

# importing a module using string name

#import "abc"    # Invalid

"""
Use exec statement 

module_name = "abc"
exec("import " + module_name) # equivalent to import abc

It compiles a string of code and passes it to the Python interpreter to be executed.
In python, the byte code compiler is available at runtime, so you can write programs that construct and run other
programs like this. 

* One drawback we see here is that, exec statement need to compile the import statement each time it runs and compiling 
is slow. 

import importlib 
modname = "XYZ
string = importlib.import_module(modname)
Another way to import to module using strings and is generally preferred way to achieve it 
"""


# TRANSITIVE MODULES RELOADS

"""
If you reload a module A and if it imports modules B and C. 
The reloaded module A will not reload the B and C , it uses the already available module of B and C.

Therefore, by default you cannot depend on reloads to pick up changes in all the modules in your program transitively,
instead, you must use multiple reload calls to update the subcomponents independently. 
"""








