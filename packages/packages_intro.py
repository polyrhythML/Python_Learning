# A directory of Python code is said to be a package.
# Such imports are known as package imports.
# Package import turns a package into a python namespace
# Package are also installed to resolve import ambiguities when a multiple program file of the same name are installed
# on a single machine.

# Directory structure is like ./dir1/dir2/module1.py

# TRY UNCOMMENTING BELOW STATEMENTS AND TRY TO ADD CHANGES AS SUGGESTED IN THE COMMENTS

# You can explicitly import module1.py without using __init__.py in dir1 or dir2
#from dir1.dir2 import module1
#print(module1.x)              # Outputs : I am in dir1.dir2.module1.py

# now add init file in dir1
#import dir1
#print(dir1.dir2.module1.x) # This will give error saying there is no module dir2 in dir1

# now add from . import dir2
# import dir1
# print(dir1.dir2.module1.x)    # This will print no module module1 in dir2

# now add __init__.py to dir2
# import dir1
# print(dir1.dir2.module1.x)    # This will print no module module1 in dir2 (no effect basically)

# now add from . import module1 to __init__.py
# import dir1
# print(dir1.dir2.module1.x)    # Outputs : 23

# Basically if you don't have an init file in the directory , the above directory where your main script is , it will
# give a warning saying that no module named dir1.Therefore, without __init__.py main script does not recognise it as a
# python module.....



# Package initialization file roles

"""
* __init__.py serves as a hook for package initialization-time actions, declares a directory as a Python package
* generates a module namespace for a directory
* safeguard against picking up a wrong directory or module, which has nothing to do with your script

from * behaviour --- > in order to list what modules to import using from abc import * , we can explicitly add module
name to the list __all__ in init.py which tells interpreter to import certain modules only when we do from abc import *

"""

# A Tale of three systems
"""
Suppose two people created two different project on the two machine under different directories 
 user1 : 
 system1 \
 utilities.py
 main.py
 other.py

 user2 : 
 system2 \
 utilities.py 
 main.py 
 other.py 

Now suppose there is a user 3 gets the code of the two users on his computer to work with.Let's say he wants to import 
utilites.py script of the system 1 user, but he also needs the utilities of the system 2 user also. What should he do ?

He can create package of the scripts from system 1 and system 2. Then he can call the utilities from both the systems 
without over writing the module name space or any kind of ambiguities...

"""


# Relative imports in the Package

"""
for import of the modules within the package requires explicit reference of the current directory reference 

# Python 3
from . import xyz  
# Python 2
import xyz  

from .xyz import abc 
"""


# Why relative imports

"""
mypkg\
    __init__.py
    main.py
    string.py

* Incase, you are trying to import string.py , how would you know whether not to pick the built in string.py or the 
module defined by the person in the scenario.
* Firstly, it is better to not have built-in module names in your script. 
* Even if you have those kinds of names, you can make a relative import 

In other words, simple imports in packages can be both ambigious and error-prone. 
Withing a package, it's not clear whether an import spam statement refers to a module within or outside the package. As
one of the consequence, a local module or package can hide another hanging directly off of sys.path, whether intentiona-
lly or not.

"""
"""
# imports string outside package
import string 
# import name from string outside the package 
from string import name 
# Imports mypkg.string here
from . import string 
# Import names from mypkg.string
from .string import name1, name2

"""

# Module lookup summary

"""
* Basic modules with simple names are located by searching each directory on the sys.path list, from left to right.
This list is constructed from both system defaults and user-configurable settings.

* Packages ae simply directories pf Python modules with a special __init__.py file, which enables A.B.C directory path 
syntax in imports.

* Within a package's file, normal import and from statements use the same sys.path search rule as imports elsewhere.
Imports in package using from statments and leading dots, however, are relative to the package, that is, only the
package directory is checked, and the normal sys.path lookup is not used. In from . import A, for example, the module
search is restricted to the directory containing the file in which this statement appears.
"""


# NAMESPACE PACKAGE !!

"""
* Allows packages to span over multiple directories ...
* Providing standard support for packages that can be split across multiple directories  and located in multiple 
sys.path entries, namespace packages both enhance install flexibility and provide a common mechanism to replace the mul-
tiple incompatible solutions that haven arisen to address this goal... 
* None of the directories taht make up a namespace package can have an __init__.py, but the content nested withing each
of them is treated as a single package.... 

import algorithm : 

--> directory\spam.py is found, a simple module is imported and returned 
--> directory\spam\__init__.py , a regular package .. 
--> directory\spam is found, and is a directory, it is recorded and the scan continues with the next directory in the 
search path. 
--> If none of the above is foundm the scan continues with the next directory in the search path. 
"""


# Example of namespace .....
"""

code\ns\dir1\sub\mod1.py
code\ns\dir2\sub\mod2.py

both the sub directories don't have any init file in them .... 
by default it become a Package namespace ... 

import sub 
sub.__path__ --> ("path to dir1\sub", "path to dir2\sub")
"""

# Nesting of the package namespace is also there, i.e. you can have more directories under dir1 which can be split
# across multiple directories but make a single package....

