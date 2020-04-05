# ADVANCE CLASSES

"""
We looked into class delegations, class compositions, class inheritance, pseudo-private attribute
DFLR, MRO methods to traverse the class for the member association to a class.
This python script we will explore
* subclass built-in types
* static methods
* slots and properties
* class decorators
* MRO, super call
"""
################### EXTENDING UTILITIES OF THE BUILT-IN CLASSES #######################################

########## 1. Extending Types by Embedding
"""
Let's code add-on utilities to the list class to add intersect, union methods in it.
"""


class List_v2:

    def __init__(self, value=[]):
        self.data = []
        self.concat(value)

    def intersect(self, other):
        res = []
        for x in self.data:
            if x in other:
                res.append(x)
        return set(res)

    def union(self, other):
        res = self.data[:]
        for x in other:
            if x not in res:
                res.append(x)
        return set(res)

    def concat(self, value):
        for x in value:
            if x not in self.data:
                self.data.append(x)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, item):
        return self.data[item]

    def __and__(self, other):
        return self.intersect(other)

    def __or__(self, other):
        return self.union(other)

    def __repr__(self):
        return "Set : {}".format(repr(self.data))

    def __iter__(self):
        return iter(self.data)


########## 2. Extending Types by Subclassing

"""
Let's try to mimic the same kind of behavior using inheritance, this time we will change the index offset used i.e. by
default the indexing starts with 0, we will start indexing it from 1
"""


class List_v3(list):

    def __getitem__(self, offset):
        print("Indexing {} at {}".format(self, offset))
        return list.__getitem__(self, offset - 1)


################### CLASS MODEL DIFFERENCE IN 2.X and 3.X #################################


"""
* In python 2.X there are two ways to code the classes, where the first version is native to the 2.X version while the
other version is called new model. The scenario is different in 3.X because both the syntaxes have been merged.

* In Python 3.X, all classes are automatically what were formerly called “new style” whether they explicitly inherit 
from object or not. Coding the object superclass is optional and implied.

* In Python 2.X, classes must explicitly inherit from object (or another built-in type) to be considered “new style” 
and enable and obtain all new-style behavior. Classes without this are “classic.”

* In Python 2.X, the identifying syntactic difference for new-style classes is that they are derived from either a 
built-in type, such as list , or a special built-in class known as object. The built-in name object is provided to serve
as a superclass for new-style classes if no other built-in type is appropriate to use.

# class newstyle(object):
    pass

* If a class defines a __getitem__ index overload method and X is an instance of this class, 
then an index expression like X[I] is roughly equivalent to X.__getitem__(I) for classic classes, but 
type(X).__getitem__(X, I) for new-style classes—the latter beginning its search in the class, and thus skipping a 
__getattr__ step from the instance for an undefined name.

* In 3.X class is itself a type and is not a generic instance object i.e. for the new way of coding the classes.
Example 
2.X                                            3.x

class C : pass                               class C : pass
I = C()                                      I = C() 
type(I)                                      type(I)
Output: <type 'instance'>                    Output: <type class '__main__.C'>

2.X with new class style

class C(object) : pass
I = C()
type(I)
Output : <class '__main__.C'>

* Above change in the class declaration brings changes in the type testing of the classes in python 2.X and 3.X
3.X                                                         2.X

>>> class C: pass                                           >>> class C: pass
>>> class D: pass                                           >>> class D: pass
>>> c, d = C(), D()                                         >>> c, d = C(), D()
>>> type(c) == type(d)                                      >>> type(c) == type(d)
False                                                       True
# 3.X: compares the instances' classes                      >>>c.__class__ == d.__class__
>>> type(c), type(d)                                        False
(<class '__main__.C'>, <class '__main__.D'>)
>>> c.__class__, d.__class__
(<class '__main__.C'>, <class '__main__.D'>)
>>> c1, c2 = C(), C()
>>> type(c1) == type(c2)
True

"""

if __name__ == "__main__":
    ###### Extending types by Embeddings

    abc = List_v2(list("trippy"))
    print(abc)
    # Output : Set : ['t', 'r', 'i', 'p', 'y']

    # Intersection operation
    print(abc & "dope")
    # Output : {'p'}

    # Union operation
    print(abc | "dope")
    # Output : {'t', 'o', 'p', 'd', 'e', 'i', 'y', 'r'}

    ###### Extending types by Subclassing

    abc_2 = List_v3("abc")
    print(abc_2)

    print(abc_2[1])
    # output :Indexing ['a', 'b', 'c'] at 1 a
    print(abc_2[2])


    ##### Example of MRO


    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B, C):
        pass

    print([cls.__name__ for cls in D.__mro__])
    # Output :['D', 'B', 'C', 'A', 'object']

