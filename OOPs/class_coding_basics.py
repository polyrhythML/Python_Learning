# Kinds of objects
# Class object - instances of class
# Instance object - instance objects processes your programs

"""

* Classes objects comes from statements whereas instance object comes from call.
* With classes each object has one copy of the independent data, supporting multiple versions of the object that the
class models.
* Class instance are similar to per-call state closure functions.
* Classes support customization by inheritance.

* self
Inside a class's method function, the first argument references the instances object being processed, assignment
to attributes of self creates or change data in the instance, not the class.

"""


class Firstclass:               # Define a class object

    def setdata(self, value):   # Define class's method
        self.data = value

    def display(self):
        print(self.data)        # self.data per instance


# Create 2 instances of the class, each have their own namespace
x = Firstclass()
y = Firstclass()

x.setdata("trippy code")
y.setdata(3.14324)
x.display()                 # Outputs : trippy code
y.display()                 # Outputs : 3.14324

# Classes are customized by inheritance

"""
* Python also allows classes to inherit from other classes, opening the door to coding hierarchies of classes that
specialize behaviour by redefining attributes in subclasses that appear lower in the hierarchy, we override the more 
general definitions of those attributes higher in the tree.In effect, the further down the hierarchy we go, the more
specific the software becomes. Here, too, there is no parallel with modules, whose attribues lives in a single, flat
namespace that is not as amenable to customization.

* Superclasses are listed in paranthesis in a class header.
* Classes inherit attributes from their superclasses.
* Instances inherit attributes from all accessible classes.
* Logic changes are made by subclassing, not by changing superclasses.
"""

class SecondClass(Firstclass):
    def display(self):
        print('Current value = "%s"'%self.data)

z = SecondClass()
z.setdata(42)       # Finds setdata in Firstclass
z.display()         # Finds overriden method in Secondclass

"""

* In the above example, the setdata attribute is fetched from the first class and the display method is fetched from 
  Second class. 
* Since, Inheritance search proceed upwards from instances to subclasses to superclasses, stopping at the first appearance
  of the attribute name that it finds. 
* Sometimes we call this act of replacing attributes by redefining them lower in the tree "overloading".

"""

# Classes are attributes in Modules

"""

* Classes are just a variable assigned to an object when class statement runs, and the object can be referenced with
any normal expression.

example : 
from modname import class1
class Class2(class1):
    def display(self):
        pass

* Class statements are run during imports to define names, and these names become distinct modules attribute.

Note : Python convention says that class name should begin with an uppercase letter, to help make them more distnct.

from person import Person 
x = person.Person()         # Here Person is a class and person is the module from which it is imported.        

"""


# Classes can intercept Python Operators

"""
* Method named with double underscore(__X__) are special hooks : 
    -> In Python classes we implement operator overloading by providing specially named methods to intercept operations.
        The python language defines a fixed and unchangeable mapping from each of these operations to a specially name 
        methods.
    -> Such methods are called automatically when instances appear in built-in operations.
        Example : __add__ method , it called whenever the object appears in a + expression.
    -> Classes can override most built in type operations.
    -> Operators allow classes to intergrate with Python's object model.
    
        
"""


class ThirdClass(SecondClass):

        def __init__(self, value):
            self.data = value

        def __add__(self, other):
            return ThirdClass(self.data + other)

        def __str__(self):
            return "[ThirdClass: %s]"%self.data

        def mul(self, other):
            self.data *= other


a = ThirdClass("abc")
a.display()

print(a)        # str return a display string for the object

b = a + "xyz"   # __add__ : makes a new instance, b has all thirdclass methods
b.display()
print(b)        # __str__ : returns string to display

a.mul(3)
print(a)        # [ThirdClass: abcabcabc]

""" 
Specially named methods such as __init__, __add__ and __str__ are inherited by subclasses and instances just like any
other names assigned in a class. If they are not coded in a class, Python looks for such names in all its superclasses.
Operator overloading methods names are also not built-in or reserved words, they are just attributes that Python looks
for when objects appear in various contexts.

Above b is the result of + operation , which results in a new object of the same type.
mul performs an in-place operation.

"""


# Why use Operator Overloading?

"""
Frankly, many operator overloading methods tend to be used only when you are implementing objects that are mathematical
in nature, a vector or matrix class may overload the addition operator,for example, but an employee class likely would
not.For simpler classes, you might not use overloading at all, and would rely instead on explicit method calls to 
implement your object behavior.
"""

# Start with simple Python Class


class Rec:
    pass


Rec.name = "Bob"
Rec.age = 40

print(Rec.name)
print(Rec.age)

"""
We see above that we can create and access attributes of a class without creating any instance of the class since 
class in itself is an object.
"""

# Let's create instance of the Rec class

x = Rec()
y = Rec()

# These instances are empty namespace objects.

print(x.name)       # Outputs : Bob
print(y.name)       # Outputs : Bob

# We see that they will obtain the attributes by inheritance.

# We see that attribute reference kicks off inheritance searches,but attribute assignments affect only the objects
# in which the assignments are made.

x.name = "trippy"

print(x.name)           # trippy
print(y.name)           # Bob

"""
Therefore we see that , attributes of a namespace objects are usually implemented as dictionaries, and class inheritance
trees are just dictionaries with links to other dictionaries.
__dict__ attribute in the namespace dictionary for most class-based objects. Some classes may also define attributes
in __slots__.
"""


print(Rec.__dict__)
# outputs : {'__module__': '__main__', '__dict__': <attribute '__dict__' of 'Rec' objects>,
# '__weakref__': <attribute '__weakref__' of 'Rec' objects>, '__doc__': None, 'name': 'Bob', 'age': 40}

print(list(Rec.__dict__.keys()))
# Outputs : ['__module__', '__dict__', '__weakref__', '__doc__', 'name', 'age']

print(list(x.__dict__.keys()))      # outputs : ['name']
print(list(y.__dict__.keys()))      # outputs : []


# To facilitate inheritance search on attribute fetch, each instance has a link to its class that Python creates
# for us

print(x.__class__)


# Classes have a reference attribute to the superclasses
print(Rec.__bases__)

# Explicit method to access a class object


def uppername(obj):
    return obj.name.upper()

print(uppername(x))         # Outputs : TRIPPY

# We can assign this simple function to an attribute of our class, though, it becomes a method, callable through any
# instance, as well as through the class name itself as long as we pass in an instance manually

Rec.method = uppername

print(x.method)  # Outputs : <bound method uppername of <__main__.Rec object at 0x000002BCF0764828>>

"""
Basically, we dont need to define a function inside a class explicitly.We can define a function outside a class 
and reference to that function using class attributes to create class methods
"""





