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


