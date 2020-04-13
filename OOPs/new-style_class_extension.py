# SLOTS

"""
* By assigning a sequence of string attribute names to a special __slots__ class attribute, we can enable a new-style
class to both limit the set of legal attributes that instances of the class will have, and optimize memory usage
and possibly program speed.The slots should be used only in applications that clearly warrant the added complexity.

* Allocating a namespace dictionary for every instance object can be expensive in terms
of memory if many instances are created and only a few attributes are required. To save
space, instead of allocating a dictionary for each instance, Python reserves just enough
space in each instance to hold a value for each slot attribute, along with inherited at-
tributes in the common class to manage slot access. This might additionally speed
execution, though this benefit is less clear and might vary per program, platform, and
Python.

"""


class limiter(object):

    __slots__ = ['a', 'b']


class D(object):

    __slots__ = ['a', 'b', '__dict__']

    def __init__(self):
        self.d = 4


############# Multiple __slot__ list in superclass ################

"""
* A name’s absence in the lowest __slots__ list does not preclude its existence in a
higher __slots__ . Because slot names become class-level attributes, instances acquire
the union of all slot names anywhere in the tree.

* If multiple classes in a class tree have their own __slots__ attributes,
generic programs must develop other policies for listing attributes. 

"""


class E:
    __slots__ = ['c', 'd']


class F(E):
    __slots__ = ['a', '__dict__']


##################### SLOT USAGE RULES ########################

"""
* Slot declarations can appear in multiple classes in a class tree, but when they do they
are subject to a number of constraints that are somewhat difficult to rationalize unless
you understand the implementation of slots as class-level descriptors for each slot name
that are inherited by the instances where the managed space is reserved.

• Slots in subs are pointless when absent in supers: 
If a subclass inherits from a superclass without a __slots__ , the instance __dict__ attribute created for the su-
perclass will always be accessible, making a __slots__ in the subclass largely pointless. 
The subclass still manages its slots, but doesn’t compute their values in anyway, and doesn’t avoid a dictionary—the 
main reason to use slots.

• Slots in supers are pointless when absent in subs: 
Similarly, because the meaning of a __slots__ declaration 
is limited to the class in which it appears, subclasses will produce an instance __dict__ if they do not 
define a __slots__ , rendering a __slots__ in a superclass largely pointless.

• Redefinition renders super slots pointless: If a class defines the same slot name as a superclass, its redefinition 
hides the slot in the superclass per normal inheritance. You can access the version of the name defined by the 
superclass slot only by fetching its descriptor directly from the superclass.

• Slots prevent class-level defaults: 
Because slots are implemented as class-level descriptors 
(along with per-instance space), you cannot use class attributes of the same name to provide defaults as you can 
for normal instance attributes: assigning the same name in the class overwrites the slot descriptor.

• Slots and __dict__: 
__slots__ preclude both an instance
__dict__ and assigning names not listed, unless __dict__ is listed explicitly too.

Conclusion : 

Slots essentially require both universal and careful deployment to be effective—because slots do not compute values 
dynamically like properties, they are largely pointless unless each class in a tree uses them and is 
cautious to define only new slot names not defined by other classes.
"""

if __name__ == "__main__":

    """
    First off, when slots are used, instances do not normally have an attribute dictionary—instead, 
    Python uses the class descriptors feature to allocate and manage space reserved for slot 
    attributes in the instance.
    """
    x = limiter()
    x.a = 1

    """
    We can still fetch and set slot-based attributes by name string using storage-neutral tools such as getattr and
    setattr and dir.
    """
    print(getattr(x, 'a'))
    # Outputs : 1
    setattr(x, 'b', 2)
    print(x.b)
    # Outputs : 2
    print('a' in dir(x))
    # Outputs : True
    """
    Also, without attribute namespace dictionary, it's not possible to assign new names to instances that are not 
    names in the slots list.
    """
    #object1 = D()
    # Output: AttributeError: 'D' object has no attribute 'd'

    """
    We can add extra member in the class by including the __dict__ in the __slot.
    Now we wont see any attribute error in the invokation of the class object D.
    """
    object2 = D()
    print(object2.d)
    # Outputs : 4
    print(object2.__dict__)             # Outputs :{'d': 4}
    print(object2.__slots__)            # Outputs :['a', 'b', '__dict__']

########## Multiple __slot__ lists in superclass ##########
    object3 = F()
    object3.a = 1
    object3.b = 2
    object3.c = 3
    print(object3.a)            # Output : 1
    print(object3.b)            # Output : 2
    print(E.__slots__)          # Output : ['c', 'd']
    print(F.__slots__)          # Output : ['a', '__dict__']
    print(x.__slots__)          # Output : ['a', 'b']


