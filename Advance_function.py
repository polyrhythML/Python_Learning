
# COUPLING EFFECT !!
# Coupling effect is something that puts together the input args and return statements together
# try to have these piece independent of the other pieces in the code
# Dont try to use the global variables in the function calls
# Try to avoid them, as much as possible,
# It makes the debugging process diffcult
# Creates dependencies and timing issues
#  Dont change the mutable objects unless required, therfore always pass the copies of the mutable objects
# Try to create a tight coupling between the caller and the callee
# Each function to be used for unified purpose
# Each function should be relatively small
# Avoid changing variables in another directory
# The more self contained a function is , its easier to understand, reuse and modify.

def sumerror(L):
    if not L :
        return 0
    else :
        return L[0] + sumerror(L[1:])


output = sumerror([1, 2, 3, 4, 5])

print(output)                       # Outputs : 15

""""
In general, we try not to use the recursive functions in python , instead use loops in python. We dont need fresh copy
of a local scope on the call stack for each iteration and avoid the speed costs associated with function call in general
"""

# Recursion can be used to traverse the indefinite shaped structures
# Python implements recursion by pushing information on the call stack at each recursive call


# CYCLES PATHS AND STACK_-LIMITS

"""
* Larger recursive calls need to avoid cycles ir repeats, record paths taken for later use 
* Avoid visiting a location which has already been visited
* If data is cyclic graph, recursive call verison will fall into an infinite recursive loop 
* Some programs also need to avoid repeated processing for a state reached more than once, even if that wouldnt lead to 
a loop.
* Some programs may also need to record complete paths for each state followed so they can repeat solutions when
finished.

sys.getrecursionlimit() ------------ > 1000 calls by default 
sys.setrecursionlimit(10000) -----------> Allows deeper nesting 
"""

# Using stacks and queues you wont need to perform such recursive call count, will have more control over the traversal

# Recursion is a powerful tool, but it tends to be best when both understood and expected

# You can pass the function objects in a list, or any of the data structures in python



print(sumerror.__name__)                    # Outputs : sumerror
print(sumerror.__annotations__)             # Outputs : {}


# Lambda
# return the function itself, instead of assigning it to a name
# called anonymous function
# lambda is an expression not statement
# can be used in the places where functions cannot be called, its inline function


x, y, z = 1, 2, 3
output = lambda x, y, z : x+y+z
print(output(1,2,4))                # Outputs : 7

# variables inside the lambda follow the variable scope as that of a normal function

dict_lambda = {"first": (lambda : 2+2),
                "second": (lambda : 2*2),
                "third" :(lambda : 2-2)
                }

X = dict_lambda["second"]
print(X())


# lambda inside lambda also possible

action = (lambda x : (lambda y : x+y ))
x = action(99)
y = x(10)
print(y)                         # Outputs : 109




