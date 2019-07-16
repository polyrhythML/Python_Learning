# This Script we will work on lists and dictionaries

# Lists are the most flexible data structure in python. It can process strings, numbers etc and even other lists
# In place changes are supported in the lists - Mutable
# Lists are ordered collections
# Variable length, Heterogeneous, and arbitrary length
# Python list reference to other objects

"""
Whenever you assign an object to a data structure component or variable name, Python always stores a reference to that
same object not a copy of it.
(unless you repeat a copy explicitly)
"""

# List comprehensions are faster way to create list
# map also does something similar, it applies built-in map function on a sequence

# Inplace Change
L = ["spam", "dfafa", "sapdds"]
L[1] = "eggs"
print(L)                        # Outputs : ['spam', 'eggs', 'sapdds']

L = [1, 2, 3]
print(L)            # Outputs : [1, 2, 3]
L[1:2] = [4, 5]
print(L)            # Outputs : [1, 4, 5, 3]         Insertion with replacement
L[1:1] = [6, 7]
print(L)            # Outputs : [1, 6, 7, 4, 5, 3]   Insertion without replacement
L[1:2] = []
print(L)            # Outputs : [1, 7, 4, 5, 3]      Insertion with replacement
L[2:5] = L[3:6]
print(L)            # Outputs : [1, 4, 5, 3]

# Above operation fetches the value to be inserted first before the deletion happens on the left
# Above operation can be used to concatenate a list in the front
L = [1]
print(L)                    # outputs : L [1]
L[:0] = [2, 3, 5]           # outputs : L [2, 3, 5]
print(L)
L[len(L):] = [6, 7, 8]      # Insert at the end of the list
print(L)                    # [2, 3, 5, 1, 6, 7, 8]
# We also have a list specific method to extend a list
L.extend([8, 9, 10])
print(L)                    # Outputs : [2, 3, 5, 1, 6, 7, 8, 8, 9, 10]

L = [2, 4, 6, 7, 8, 3, 5]
print(L.sort())             # Outputs : None
# Sort basically sorts the list inplace and it doesnot return the list

print(L)                    # Outputs : [2, 3, 4, 5, 6, 7, 8]

L = ["abc", "ABC", "aBc"]
L.sort()
print(L)                    # Outputs : ["ABC", "aBc", "abc]

# We can also specify the key , basis on which we want to sort

L.sort(key=str.lower)
print(L)                    # Outputs : ["ABC", "aBc", "abc]
L.sort(reverse=True)
print(L)                    # Outputs : ["abc", "aBc", "ABC"]

# Sort is useful when when sorting list of dictionaries , to pick out a sorted key
"""
WARNING : As mentioned above , sort and append changes the list in place , and doesnot return the list itself.
Therefore, we got the result as None above 
Hence, we also have built-in method - sorted
"""
print(sorted(L, key= str.lower, reverse=True))      # Outputs : ["abc", "aBc", "ABC"]

# Hence above is the explanation why sorted is preferred over sort

del L[0]            # Deletes one element
del L[1:]           # Deletes a section
L[1:] = []          # Deletes a section as above

# Difference between assigning [] to slice and an element

L = [1, 3, 5, 7, 2, 6]
L[1:] = []
print(L)                        # Outputs : [1]
L = [1, 3, 5, 7, 2, 6]
L[1] = []
print(L)                        # Outputs : [1, [], 5, 7, 2, 6]


# DICTIONARIES ------------------------------------- >

# Arrays or hashes
# Associate a set of values with keys
# Unordered Collections
# Variable length, heterogeneous, and arbitrary nestable
# mutable mapping
# can be changed in-place
# are unordered collections of objects referenced by keys
# Internally dictionaries are implemented as hashtables

D = {}
A = {"abc": "xyz", "123": "a61"}
E = {"cto": {"name": "Bob", "age": 40}}
B = dict(name="bob", age=40)
A.update({"25": "myupdate"})
print(A)                       # Outputs : {'abc': 'xyz', '123': 'a61', '25': 'myupdate'}
A.update({"abc" : "2452"})
print(A)                       # Outputs : {'abc': '2452', '123': 'a61', '25': 'myupdate'}

# As we see above , update() overwrites the value of the key already present in the dictionary


"""
ordered_dict : gives dictionary with order, but they are hybrids that incur extra spaces and space
overheads to achieve their extra utility and are not true dictionaries.
Basically, Keys are kept redundantly in a linked-list tp support sequence ops
"""
# Dictionaries are best for quick lookups instead of linear searches

print({k: 0 for k in ["a", "b", "c"]})           # Outputs : {'a': 0, 'b': 0, 'c': 0}
D = dict.fromkeys("spam")
print(D)                    # Outputs : {"s": None, "p": None, "a": None, "m": None}

print(D.keys())             # Outputs : dict_keys(['s', 'p', 'a', 'm'])
print(D.values())           # Outputs : dict_values([None, None, None, None])
print(D.items())            # Outputs : dict_items([('s', None), ('p', None), ('a', None), ('m', None)])



















