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


# Iterable Objects

"""
*All iteration contexts in Python will try the __iter__ method first, before trying __getitem__.That is, they prefer the
iteration protocol to repeatedly indexing an object, only if the object does not support the iteration protocol is
indexing attempted instead.

* You should prefer __iter__ too, it supports general iteration context better than __getitem__ can.

* Iterable object - iter() - > iterator object -> iter.__next__()  -> until -> stop iteration
* 
"""


# Let's look at the an user defined iterable class

class Squares:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2


for i in Squares(1, 5):
    print(i)                    # Outputs : 1 4 9 16 25

"""
the iterator object returned by __iter__ is simply the instance self, because the __next__ method is a part of this
class itself. In more complex scenarios, the iterator object may be defined as a separate class and object with its own
state information to support multiple active iterations over the same data.
"""

X = Squares(2,5)
I = iter(X) # --> This I
print(next(I))      # Outputs : 4
print(next(I))      # Outputs : 9


S = "dadf"

for x in S:
    for y in S:
        print(x+y, end=" ")

# Outputs : dd da dd df ad aa ad af dd da dd df fd fa fd ff
# Each iterator has its own state information as shown in the above example.


# To support the multiple-iterator effect, __iter__ simply needs to define a new stateful object for the iterator,
# instead of returning self for each iterator request.




# __iter__ plus yield

"""
As an added bonus the state of instance attributes + local variables both is retained in the case where the generator 
functions are used inside a class...
"""

# Example of generator :

def gen(x):
    for i in range(x):
        yield i**2
G = gen(5)
I = iter(G)

print(next(I), next(I), next(I))

# Let's code a class with generator function which yields a value


class Squared_gen:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):                                     # __next__ is implicit
        for value in range(self.start, self.stop + 1):
            yield value ** 2


for i in Squared_gen(1, 5):
    print(i)                    # Outputs : 1 4 9 16 25

S = Squared_gen(1, 5)
I = iter(S)
print(next(I))                  # Outputs : 1
print(next(I))                  # Outputs : 4


# We can also create a generator function without iter , just we would have to wrap it around iter to creater an
# Iterator

"""
* With __iter__, iteration triggers __iter__, which returns a new generator with __next__.
* Without __iter__, it returns itself for __iter__. 
"""

# Iter-yield combination to be used when you dont want to explicitly code __next__ and __iter__
