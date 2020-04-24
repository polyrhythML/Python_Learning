# Overview

"""
* Events which modify the flow of control through a program.
* try/except : Catch and recover from the exception in python
* try/finally : Perform a cleanup action, whether exception occurs or not.
* assert : Conditional trigger an exception in your code.
* raise : Trigger an exception manually in your code.

Why use exceptions ?
* If your function executing fails, exception routes the code run to an alternate path.
"""

# try/except/else
"""
try:                    
    statements          # Run this main action first 
except name1:               
    statements          # Run if name1 is raised during try block
except (name2, name3):
    statements          # Run if any of these exceptions occur
except name4 as var:
    statements          # Run if name4 is raised, assign instance raised to var
else:
    statements1         # Run if no exception was raised during try block


• If an exception occurs while the try block’s statements are running, and the ex-
ception matches one that the statement names, Python jumps back to the try and
runs the statements under the first except clause that matches the raised exception,
after assigning the raised exception object to the variable named after the as key-
word in the clause (if present). After the except block runs, control then resumes
below the entire try statement (unless the except block itself raises another ex-
ception, in which case the process is started anew from this point in the code)

• If an exception occurs while the try block’s statements are running, but the ex-
ception does not match one that the statement names, the exception is propagated
up to the next most recently entered try statement that matches the exception; if
no such matching try statement can be found and the search reaches the top level
of the process, Python kills the program and prints a default error message.

• If an exception does not occur while the try block’s statements are running, Python
runs the statements under the else line (if present), and control then resumes below
the entire try statement.

* We can code else only if an exception has been encountered.

* The empty except clause is a sort of wildcard feature—because it catches everything, it
allows your handlers to be as general or specific as you like. In some scenarios, this
form may be more convenient than listing all possible exceptions in a try .

* Empty except s also raise some design issues, though. Although convenient, they may
catch unexpected system exceptions unrelated to your code, and they may inadver-
tently intercept exceptions meant for another handler.

* else used with try and except because it removes unambiguity whether an exception was
encountered or not. Since it is only executed if the try statment was passed without any
exception handling.

*  
"""

# Try except


def try_except():

    def kaboom(x, y):
        print(x + y)

    try:
        kaboom([0, 1, 2] + "spam")
    except TypeError:
        print("Hello world")
    print("Resuming here")

"""
once you’ve caught an error, control resumes at the place where you
caught it (i.e., after the try ); there is no direct way to go back to the place where the
exception occurred (here, in the function kaboom ).
"""


def try_finally():

    def stuff(file):
        raise MyError()
    file = open("data", 'w')

    try:
        stuff(file)
    finally:
        file.close()
    print("not reached")

"""
* The code in this statement’s main-action block is executed first, as usual. If that code
raises an exception, all the except blocks are tested, one after another, looking for a
match to the exception raised. If the exception raised is Exception1 , the handler1 block
is executed; if it’s Exception2 , handler2 is run, and so on. If no exception is raised, the
else-block is executed.

* No matter what’s happened previously, the finally-block is executed once the main
action block is complete and any raised exceptions have been handled. In fact, the code
in the finally-block will be run even if there is an error in an exception handler or the
else-block and a new exception is raised.

* As always, the finally clause does not end the exception—if an exception is active
when the finally-block is executed, it continues to be propagated after the finally-
block runs, and control jumps somewhere else in the program (to another try , or to
the default top-level handler). If no exception is active when the finally is run, control
resumes after the entire try statement.

The net effect is that the finally is always run, regardless of whether:
• An exception occurred in the main action and was handled.
• An exception occurred in the main action and was not handled.
• A new exception was triggered in one of the handlers.
• No exceptions occurred in the main action.

"""

def merged_exceptions():

    sep = "-"*45 + "\n"

    print(sep + "Exception RAISED AND CAUGHT")
    try:
        x = "spam"[99]
    except IndexError:
        print("Except Run")
    finally:
        print("Finally Run")

    print("After run")

    print(sep+"NO EXCEPTION RAISED WITH ELSE")
    try:
        x = "spam"[3]
    except IndexError:
        print("Except run")
    else:
        print("Else Run")
    finally:
        print("Finally Run")
    print("After Run")

    print(sep + "NO EXCEPTION RAISED")
    try:
        x= "spam"[3]
    except IndexError:
        print("Except run")
    finally:
        print("Finally run")
    print("After Run")


if __name__ == "__main__":

    merged_exceptions()
