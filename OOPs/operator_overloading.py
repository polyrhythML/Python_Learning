#OPERATOR OVERLOADING

"""
Intercepting built-in operations in a class's methods.

* Operators overloading lets classes intercept normal Python operations.
* Classes can overload all Python expression operators.
* Classes can also overload built-in operations such as painting, function calls, attribute access etc.
* Overloading makes class instances act more like built-in types.
* Overloading is implemented by providing specially named methods in a class.

"""

"""
Instance creation : 
* Instance creation first triggers the __new__ method, which creates and returns the new instance object,which is then 
passed into __init__ for intialization.Since __new__ has a built-in implementation and is redefined in only very limited
roles,nearly all Python classes initialize by defining an __init__ method.

Not present by default : 
* Operator overloading methods may be inherited from superclasses if not defined, just like any other methods. Operator
overloading methods are also all optional, if you don't code or inherit one, that operation is simply unsupported by
your class, and attempting it will raise an exception. Some built-in operations, like printing, have defaults,but most
built-in fail for class instances if no corresponding operator overloading method is present.

SPEED 
* overloaded function calls are slower compared to the builtin functions for the same operation.
* The overhead of a function call comes is what makes it slower compared to the built-in cases.


"""

# __getitem__
# __getitem__ is used for the instance-indexing operations


class Indexer:
    def __getitem__(self, index):
        return index**2


X = Indexer()
print(X[2])             # Outputs : 4

for i in range(5):
    print(X[i], end=" ")        # Outputs : 0 1 4 9 16

# __getitem__ performs two operations , indexing and slicing, both of which can be known with argument type passed


class Indexer:
    data = [5, 6, 7, 8, 9]

    def __getitem__(self, index):
        if isinstance(index, int):
            print("getitem:", index)
        else:
            print("Index Attributes : ", index.start, index.stop, index.step)
        return self.data[index]

X = Indexer()
print(X[2])         # Outputs : getitem: 2 7

print(X[2:4])       # Outputs : 2 4 none [7, 8]
