import sys
# Well I am back after a break of 2 weeks, Let's start with Modules and Packages

# Each Python file is a module and each module can be called by another module
# Can be imported using two keywords
# import X  -> it imports the whole module
# from X import Y  -> imports a specific function or class from the module


"""
In short modules provide as easy way to organize components into a system by serving as a self contained package of
variables known as namespaces.
Ultimately, Python's modules allow us to link individual files into a larger program system.
* Code reuse
* System namepace partitioning
"""

# Let's try to understand concept of imports and attributes with an example

# Let's say this is our top level script
# I am going to create a script/module b.py which we will import here
# look into the code of b.py to see what it has

import b
b.spam("imported")          # Outputs : imported spam

# We can also can chain/ hierarchy of the modules to use import into one another
# Python itself has more than 200 modules, called the standard library, which can be used on any platform where you are
# trying to run python.

# HOW IMPORT WORKS
"""
* Much similar to the C programmers like to compare the Python module import operation to a C #include, but they 
really shouldn't . In Python, imports are not just textual insertions of one file into another. They are really runtime
operations that perform three distinct steps the first time a program imports a given file.

* find module's file 
* compile to bytecode
* Run the module's code
Note : 
After first time loading the module through import, python doesnot perform the above three steps again, it stores the
loaded module in a table names sys.modules

"""

# HOW COMPILE WORKS

"""
* During import operation Python checks both file modification times and the byte code python's version to proceed.
* modification time --> timestamp.
* Version number --> uses number embedded in the byte code or a filename, depending on Python release.

* When to compile : 
> if the byte code for the module is older and you have regenerated the main program file
> In python 3.2 and above we have __pycache__ subdirectory and named with their Python version  to avoid contention
and recompiles when multiple Pythons are installed.

* When not to compile :
> If the pyc byte code file that is not older than the corresponding .py source file and was created by the same
Python version, it skips the source code to byte code compile step.

"""

# __pycache__ speedups in startups

"""
*Previously, python use to compile modules, for the run-time of the program, keep it in memory and then release the
memory after the program got terminated.
But to speed up the program run next time too, python will try to save the bytecode in a file in order to skip the 
compile step next time around.

*pycache dir --> one for each of the module directory, has more descriptive method of saving pyc , saves the version
number.

OVERALL PYTHON ALWAYS RECREATES the bytecode file you have changes the source file since the last compile,
but the version differences are handled python 3.2 prior and above.
"""

# NOTE : Under the model used in python 3.2 and later, importing the same file with a different Python creates
# a different bytecode file, instead of overwriting the single file as done by the pre-3.2 model, in the newer model,
# each Python version and implementation has its own byte code files, ready to be loaded on the next program run.


# HOW TO SEARCH FOR THE MODULE PATH

"""
* Home directory of the program ---> directory of the top level script
                                ---> overrides the module names anywhere else, if it is present in the current folder
* PYTHONPATH directories
        ---> secondly, it looks for all the files listed in your PYTHONPATH environment variable setting, from left to
        right.
PYTHONPATH files are basically , list of user-defined and platform specific names of the directories that contains
Python code files.
        ---> If you need to import a file that is stored in a different directory from the file that imports it.
        You woudl probably want to use PYTHONPATH variable once you start writing substantial programs
"""


print(sys.path) # --> this is basically the list of path files which python looks into when it searches on each import
                # of a new file.


# An import statement of the form import b might today load or resolve to :
"""
* Source code file b.py
* bytecode file b.pyc
* An optimized bytecode file named b.pyo
* A directory named b, for the package imports
* A compiled extension module, coded in C, C++, or another language and dynamically linked when imported
* A compiled built-in module coded in C, and statically linked to python 
* A ZIP component that is automatically extracted when imported
* An in-memory image, for frozen executables
* A java class, in the Jython version of the python 
* A .NET component, in the IroPython version of Python

"""

# SELECTION PRIORITY
"""
*If you have b.py and b.so in different directories, Python will always load the one found in the first(leftmost)
directory of your module search path during the left ot right search of the sys.path

* But if the b.py and b.so are in the same directory, it will search for the -- > it has a standard picking order
"""

