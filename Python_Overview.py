# Python is an interpreted language

"""
* Python stores the  bytecode in pycache for start speed optimization.
The next time you run your program , Python will load .pyc files and skip the compilation step.
* Python automatically checks last modified time-stamp of the source.
* Note : that the bytecode is saved for the files which are imported and not for the 
 top level, files of a program that are only run as scripts.

 ----------------------- PVM ------------------------------ > 
 * PVM is a big code loop that iterates through your byte-code instructions, one by one, to 
 carry out their operations
 * Python byte-code is not binary machine code, it is a Python specific representations

 ------------------ Python Implementations ---------------- > 

 * Cpython (Mostly used) 
 * Jython 
 * IronPuthon 
 * Stackless 
 * Pypy

* Jython and Iron Python completely indepenedent implementation of the Python that compiles
 python source from different architectures, to provide direct access to the Java and .net
 components.
* Frozen binaries - Standalone binary executables 
	              - these can be run without requiring a python installation
Frozen binaries - bytecode + PVM + support files needed to run a single package


"""