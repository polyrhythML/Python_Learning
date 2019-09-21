# ITERATIONS - one of the most important concepts in Python

# An object is iterable if it is
# 1 - a physically stored sequence
# 2 - an object that produces one result at a time in the context of an iteration tool

# Physical sequences and virtual sequences created on demand
# __next__ method to advance to next element and catching the StopIteration exception when to exit

# Iteration runs at C language speed inside Python, whereas the while loop version runs Python bytecode through
# Python virtual machine

# X.__next__() ---- > 3.X
# next(X) -- > general method across python 3.X and 2.X

# Basically, iterable object return an iterator object which has next method

# Iterable
L = [1, 2, 3]
# Iterator
I = iter(L)
print(I)                # Outputs : <list_iterator object at 0x0000020C26AA0E10>
print(I.__next__())     # Outputs : 1
print(I.__next__())     # Outputs : 2
print(I.__next__())     # Outputs : 3

# It checks for the end of the list , and exits the iteration protocol

# List comprehensions run faster than manual for loop statements because their iterations are performed at C
# language speed inside the interpreter, rather than with manual Python code.

# [ x+y for x in "abc for y in "lms"]    [expression (outer) (inner)]
# [expression (for loop ) (if condition)]

# sorted(), zip(), map(), enumerate(), filter(), reduce() ... all accept iterable
# lists, tuples ... all accept iterables

"""
Note : when to use extend or append 
extend iterates automatically, but append doesnot, use the latter to add an iterable to a list without iterating 

"""