# We will see how much procrastination  is there in python
# Generator are the hormones which makes python procrastinate
# That was pretty lame , i know

# Generator functions -> which yields values at demand, suspending their state and resuming it afterwards
# Generator expression -> much like comprehensions , return an object that produces results on demand

# They basically save memory and allow computation time to be split across the result requests.

# They are able to pull of this magic using iteration protocol in python

"""
STATE SUSPENSION :
* The state that generator function retains, saves the memory location of the code and the local variable scope.
Hence, the local variables retain the information between results, and make it available when the functions are
resumed.

"""

"""
ITERATION PROTOCOL : 
* Iterator objects define a __next__ method which returns the next item in the iteration, or raises the special 
Stop iteration exception to end the iteration.
* An iterable object is fetched with the built-in iter function. This iter operation is no-op for the objects which
their own iterator

"""


# Let's get into some lazy action

def square(N):
    for i in range(N):
        yield i **2

a = square(5)
print(a)                                # Outputs : <generator object square at 0x0000022D156CD390>
print(a.__next__())                     # Outputs : 0
print(a.__next__())                     # Outputs : 1

for i in square(5):
    print(i, end=" : ")

# We can make a function explicitly iterable by applying iter function over it

y = square(10)
x = iter(y)
print(iter(y) is y)                     # Outputs : True
# Hence, we see that y is an iterable object



