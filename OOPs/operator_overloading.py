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



# ATTRIBUTE ACCESS : __getattr__ and __setattr__

# The dot operator expression can be implemented by our code too, for reference, assignment and deletion contexts.
"""
__getattr__ method intercepts attribute reference. It's called with the attribute name as string whenever you try to
qualify an instance with an undefined attribute name. It is not called if python can find the attribute using its 
inheritance tree search procedure.
"""


class Empty:
    def __getattr__(self, attrname):
        if attrname == "age":
            return 40
        else:
            raise AttributeError(attrname)


X = Empty()
print(X .age)


# Attribute Assignment and Deletion

"""

* __setattr__ intercepts all attribute assigments. If this method is defined or inherited, self.attr = value becomes
self.__setattr__("attr", value)

* This allows your class to catch attribute changes, and validate or transform as desired.
 
"""


class Accesscontrol:
    def __setattr__(self, attr, value):
        if attr == "age":
            self.__dict__[attr] = value + 10
        else:
            raise AttributeError(attr + "not allowed")


X = Accesscontrol()
X.age = 40
print(X.age)
#X.name = "Bob"          Outputs : Attribute Error : name not allowed

"""
__DEL__ATTR__ 

* A third attribute management method, __delattr__. is passed the attribute name string and invoked on all attribute
 deletions.Like __setattr__, it must avoid recurvise loops by routing attribute deletions with the using class through
 __dict__ or a superclass.
"""

"""
* Thus above three attribute access overloading methods allow you to control or specialize access to attributes in your 
objects.They tend to play highly specialized roles.

* The __getattribute__ method intercepts all attribute fetches, not just those that are undefined, but when using it 
you must be cautious than with __getattr__ to avoid loops.

* The property built-in function allows us to associate methods with fetch and set operations on a specific class 
attribute. 

* Descriptor provide a protocol for associating __get__ and __set__ methods of a class with access to a specific class 
attribute.

We will have a look at them in a later script!!!

"""

# EMULATING PRIVATE MEMEBER IN A CLASS


class PrivateExc(Exception):
    pass


class Privacy:
    def __setattr__(self, attrname, value):
        if attrname in self.privates:
            raise PrivateExc(attrname, self)
        else:
            self.__dict__[attrname] = value


class Test1(Privacy):
    privates = ["age"]


class Test2(Privacy):
    privates = ["name", "pay"]

    def __init__(self):
        self.__dict__["name"] = "Tom"

# Uncomment the the below multi-line comment to run the above class
# Comment rest of the code below the comment

"""

if __name__ == "__main__":

    x = Test1()
    y = Test2()

    x.name = "Bob"  # Works
    y.name = "sd"   # fails

    x.age = 30      # Works
    y.age = 40      # Fails

"""


class adder:

    def __init__(self, value=0):
        self.data = value

    def __add__(self, other):
        self.data += other


x = adder()
print(x)            # OUTPUT : <__main__.adder object at 0x00000220D3054C18>

# Coding a str repr method allows us to customize the display as in the following , which defines a __repr__ method
# in a subclass that returns a string representation for its instances.


class addrepr(adder):
    def __repr__(self):
        return "This is how you represent something {}".format(self.data)


x = addrepr(2)
print(x)            # This is how you represent something 2
x+1
print(x)            # This is how you represent something 3
print(str(x))       # This is how you represent something 3
print(repr(x))      # This is how you represent something 3


"""

* __repr__ is used everywhere except by print and str when a __str__ is defined.This means you can code a __repr__ to
define a single display format used everywhere.
* __str__ use to support print statement support.
* __str__ overrides __repr__ ....
"""

# To ensure that a custom  display is run in all contexts regardless of the container, code __repr__, not __str__


class Printer:
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return str(self.val)


objs = [Printer(2), Printer(3)]
for x in objs:
    print(x)

# Output :  2
# Output :  3

# __radd__ -> to implement 1 + y without any error
# __iadd__ -> to implement implict += operator
# __mul__ , __rmul__ and __imul__ is same as the above explained operators pretty much ....


class Number:
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return str(self.val)

    def __iadd__(self, other):
        self.val += other*2
        return self


x = Number(5)
x +=1
print(x)            # Outputs : 7

# Let's change the way we __call__ method for function call expressions applied to your instances


class Callee:
    def __call__(self, *args, **kwargs):
        print("This is to announce that the instance has arrived")
        print("Called {}, {}".format(*args, *kwargs))


C = Callee()
C(1, 2, 3)                  # Outputs : This is to announce that the instance has arrived
                            # Called 1, 2

# __gt__  -> greater than operator
# __lt__  -> less than operator
# __cmp__ -> for any of the comparison operator


class Comp:
    def __init__(self, val):
        self.val = val

    def __gt__(self, other):
        return self.val == other

    def __lt__(self, other):
        return self.val > other


c = Comp(3)
print(c > 3)        # Outputs : True, See how we have changed the meaning of the comparison operator itself.
print(c < 2)        # Outputs : True, We made the less than operator perform the operation of
                    # the greater than operator

# BOOL and LEN
# Bool tries to infer object being true or false
# Len tries to infer the length of the object


class Truth:
    def __bool__(self):
        return True


t = Truth()
if t:
    print("Truth is truth !!")      # Above condition works

# If bool method is missing python falls back to the length because a nonempty object is considered true.
# i.e. a nonzero length is taken to mean the object is true, and a zero length means it is false....


class Ltruth:
    def __len__(self):
        return 0


l = Ltruth()

if not l:
    print("Yeah it works")

# If both bool and len are present, Bool is used over len.....
# If neither of the methods are defined then the object vacuously is considered as True

# Deleting an object instance

"""
* We saw how __new__ is called in python while we are initializing a class and calling its constructor.
* Similarly, destructor method __del__ is run automatically when an instance's space is being reclaimed --- > garbage
collection.
"""


class Life:
    def __init__(self, name="unknown"):
        print("Hello" + name)
        self.name = name

    def live(self):
        print(self.name)

    def __del__(self):
        print("Goodbye Macha {}".format(self.name))


trippy = Life("code")       # Outputs : Hellocode
trippy.live()               # Outputs : code
trippy = "new code"         # Outputs : Goodbye Macha code


















