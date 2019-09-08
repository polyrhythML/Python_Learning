# Since module names are follow same rules as any other variable name in the imported script.
# We need to be careful not to choose names the names which might clash with the keywords in python.

# For example, for if.py you will get import error because if is a reserved word in python
# Therefore, both the names of module files and the names of directories used in package imports must conform...

# Extension Modules
"""
It is also possible to create a python module by writing code in an external language such as C, C++ and others.
Such modules are called extension modules, and they are generally used to wrap up external libraries for use in Python
scripts.

"""

# Difference between import and from
"""
import fetches the module as a whole, so you must qualify to fetch its names, in contrast, from fetches specific names
out of the module.

"""

# import serves two purposes, it identifies an external file to be loaded, and it becomes a variable in the script
import os
print(os.getcwd())

# importing a specific attribute of the module
from os import getcwd
print(getcwd())

# We can use from to import all the attributes of a module by using from X import *


# IMPORT ONLY HAPPENS ONCE
"""
Modules are loaded and run on the first import or from, and only the first. This is on purpose because importing is an
expensive operations, by default Python does it just only once per file, per process. Later import operations simply
fetch the already loaded module object.(which is not the case with Python 3.x onwards)
"""

import simple
# When you run the code till above statement, prints hello , look into simple.py script
# the variables defined in the script simple.py is initialized at import time

print(simple.spam)
"""
later runs of the import don't rerun the module's code.They just fetch the already created module object from Python's 
internal modules table.
"""

# You can rerun the import of a module , but for that you need to use reload function.

# import and from are executable statements, not compile time declarations


# MUTABLES WITH MODULES

from small import x, y
x = 42          # Here x is a local copy of x and does not affect the actual variable in x
y[0] = 42       # Here y[0] is referencing to the actual list object present in the small.py

# To actually change global name in another module, you need to use import

import small

small.x = 35 # Changes the x in small.py too


"""
from module import name1, name2

Equivalent to : 

import module
name1 = module.name1
name2 = module.name2 
del module
"""


"""
Hence, the from statement creates new variables in the importer, which initially refer to object of the same names in
the imported file. Only the names are copied out, though not the objects they reference, and not the names of the module
itself.When we use the from * form , all the top-level names in the module are copied over to the importing scope this 
way. 
"""


# Pitfall of the from statement

"""
* potential to corrput namespaces of the variables in the current script/scope.
* This does not happen with the import since you have to go through the module.name to get its content
* Also, if reload is used, particular script might be accessing an older version of the variable, which gets updated
with from statement.
"""

# Generally prefer import statement simple modules

"""
Example : 

# M.py 
def func()

# N.py 
def func()

# Z.py 

from M import func
from N import func  # This overwrites the func from M
func()              #Call N.func only 

Otherhand, 

import M , N
M.func()
N.func() # No overwriting 

"""


# Another way out is using name extension
# from M import func as func1
# from N import func as func2


# Few points about Namespaces

"""
* module statements run on the first import 
* Top-level assignments create module attributes
* Module namespaces can be accessed via the attribute __dict__ or dict(object)
"""

# Attribute name qualification
# X means search for X in the current scope
# X.Y means in the current scope look for X and then search for attribute Y in the object
# X.Y.Z in the current scope of X, look for Y and then look for Z in the object X.Y


# Imports Vs Scopes
"""
A variable's meaning is always determined by the locations of assignment in your source code, and attribute are always
requested are always requested of an object explicitly.
"""

# Reloading Modules ...

"""
Why reload is required ?

* Dynamic customization, in case of GUI interface designing and testing.
* Changing parts of the program without stopping the code.
* Currently, reload works on only the modules written in python and not for extension modules 

Some basics : 

* Reload expects an object to be already loaded. 
* syntax - > 
from imp import reload 
reload(module_name)

* When you reload a module, python reruns the file's source code and reruns its top level statements.
NOTE: reload changes the objects in place and does not delete and re-creates the module object.Therefore, any reference 
to any of the object of that particular module is affected by the reload operation.

* reload runs a module file's new code in the module's current namespace.
* Top-level assignments in the file replaces names with the new values.
* Reloads impact all clients that use import to fetch modules.
* Reload apply to a single module only. 

NOTE : You would want to pair your reload with import and not from, as the latter isn't updated by reload operations
"""


# USEFULNESS :

"""
* Module reloads are also useful in larger systems , especially when the cost of restarting your systems/ entire appli-
cation is prohibitive.
* Dynamic reloads of the systems without closing the applications....
"""

