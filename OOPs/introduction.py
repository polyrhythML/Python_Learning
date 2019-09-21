# Starting with OOPs here

"""
* Inheritance - base class properties to be used as a base for other classes. Eg Robot base class for basic definition
* Composition - Robot can lift , walk , respond and further perform many other tasks. So all these tasks become diff
pieces of classes.

* Classes are another python programming units.In fact, classes also define new namespaces, much like modules.But,
compared to other programs units we've already seen, classes have three critical distinctions that make them useful
when coming to building new sytems.

    * Mulitple instances
        * Classes generates more than one object.Every time we call a class, we generate a new object with a distinct
        namespace.Each object generated from a class has access to the class's attribute and gets a namespace of its
        own for data that varies per object.
        This is quite similar to the state retention of closure functions,but is explicit .

    * Customization via inheritance
        * we can extend a class by redefining its attributes outside the class itself in new software components
        coded as subclasses.More generally, classes can build-up namespace hierarchies, which define names to be
        used by objects created from classes in the hierarchy.

    * Operator Overloading
        *By providing special protocol methods, classes can define objects that respond to the sorts of operations
        we saw of operations we saw at work on built-in types. For instance,objects made with classes can sliced,
        concatenated, indexed and so on. Python provides hooks that classes can use to intercept and implement any
        built-in types.



"""


# Attribute inheritance search

"""
* In python, attribute fetch are simply tree searches.The term inheritance is applied because objects in a tree 
attributes attached to objects higher in that tree.
As the search proceeds from the bottom up, in a sense, the objects linked into a tree are the union of all attributes
defined in all their tree parents, all the way up the tree. 

* We build up trees of linked objects with code, and Python really does climb this tree at runtime searching for
attributes every time we use the object.attribute expression.

"""


#Class
"""
* Serves as an instance factory.Their attributes provide behaviour- data and functions that is inherited by all
instances generated from them. 
"""

# Instance
"""
* Represents the concrete items ina program's domain.Their attributes record data that varies per specific object.
"""

# Redefinition is at the heart of software customization in OOP --by redefining and replacing the attribute.


# CLASSES AND INSTANCE

"""
* We only ever have one instance of a module in memory, but with classes we have many instances..
* Operationally, classes will usually have functions attached to them, and the instances will have basic data items
used by the class's functions classic data-processing.
* Infact, the object oriented model is not that different from the records with data, and classes are the programs 
for processing those records.In OOP,though, we also have the notion of an inheritance hierarchy, which supports
software customization better than earlier models.

 
"""

# CODING CLASS TREES


class C2:
    pass


class C3:
    pass

# Multiple Inheritance (left to right order of priority )


class C1(C2, C3):
    pass


I1 = C1()
I2 = C1()

"""
Attributes attached to instances pertain only to those single instances, but attributes attached to classes are shared
by all their subclasses and instances.

* Attributes are usually attached to classes by assignment made at the top level in class statement blocks, and not
nested inside function def statement there.
* Attributes are usually attached to instances by assignment to the special argument passed to the functions coded 
inside the class, called self.

"""



# OPERATOR OVERLOADING!


class C2:
    pass


class C3:
    pass


class C1(C2, C3):
    def __init__(self, who):
        self.name - who


I1 = C1('bob')
I2 = C1('sue')


print(I1.name)



# __init__() by default method call when a class's instance is generated --- constructor
# If no init is present , class return an empty instance, without initializing it


# OOP is about Code Reuse :

"""
* Classes may also provide their own implementations of operations such as indexing, fetching attributes, printing
and more.
* With classes we code customized existing software, which can be used by people for general purpose. 
* 
"""


# Polymorphism

"""
* Means an operation depends on the object being operated upon. Code should not care about what an object is rather
care about what that object does.

"""

# FRAMEWORK A WONDER OF CLASSES

"""
In many application domains, you can fetch or purchase collection of super classes, known as frameworks,that
implement common programming tasks as classes, ready to be mixed into your applications.These frameworks might provide
database interfaces, testing protocols, GUI toolkits, and so on. With frameworks, you often simply code a subclass that 
fills in an expected method or two. The framework classes higher up in the tree do most of the work for you.
"""