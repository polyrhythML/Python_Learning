"""
We will be coding two python classes , where first class would be Person and we will have methods defining the
properties of a Person.
Then we will have a class called Manager which will inherit properties from Person and will have Properties of its own
and then we will build a database to leverage these classes and store real world datapoints as entities.
"""


class Person:
    # We certainly need to pass a name to create instance of this class, rest job and Pay have a default
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    # Add some behavior methods
    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    # Adding operator overloading functionality using __repr__
    # Instead of printing all the attributes explicitly (bob.name, sue.name)
    # Class's instance object should be printing this....
    def __repr__(self):
        return "[Person : {} {} {}]".format(self.name, self.pay, self.job)


class Manager(Person):
    # Let's say manager receives a bonus apart from percent raise
    # A class's method can always be called either through an instance or through the class
    # Below code uses the person's give raise method , to reduce workarounf give raise function if the function needs
    # to be changed in the future...
    def __init__(self, name, pay):
        Person.__init__(self, name, "mgr", pay)

    def give_raise(self, percent, bonus=0.10):
        Person.give_raise(self, percent + bonus)


"""
WE see that bob and sue are both independent and different namespace object.They each have their own independent copy of
the state information created by the class.Because each instance of a class has its own set of self attributes, classes 
are a natural for recording information for multiple objects this way.
"""


if __name__ == "__main__":
    # Self test code
    bob = Person("Bob Smith")
    sue = Person("Sue Jones", job="dev", pay=100000)
    tom = Manager("Tom Jones", 500000)
    """
    print(bob)          # Outputs :  [Person : Bob Smith 0]
    print(sue)          # Outputs :  [Person : Sue Jones 100000]
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    print(bob.last_name(), sue.last_name())
    bob.give_raise(0.10)
    sue.give_raise(0.2)
    print(bob.pay, sue.pay)
    # Since manager has no init constructor, it inherits from the person's class
    tom = Manager("Tom Jones", "mgr", 500000)
    tom.give_raise(0.10)
    print(tom.last_name())
    print(tom)

    """
    for obj in [bob, sue, tom]:
        # polymorphism depending upon the type of class, give_raise function is called...
        # Overloading, you change the signature of the method - same here
        # Overidding, same signature but calling different version through inheritance
        obj.give_raise(0.10)
        print(obj)

    # Outputs : [Person : Bob Smith 0]
    #           [Person : Sue Jones 110000]
    #           [Person : Tom Jones 600000]


# Some Points to Ponder about OOPs

"""

Here we saw and example of a piece of code which implements OOPs
* Instance creation - filling out instance attributes 
* Behavior methods - encapsulation of logic in a class's methods 
* Operating overloading - providing behavior for built-in operations
* Customizing behavior - redefining subclasses 
* Customizing constructors - adding initialization logic to superclass steps 
 
"""

# USING INTROSPECTION TOOL !!

"""
* Instance.__class__  -> provides a link from an instance to the class from which it was created.
* Classes in turn have a __name__, just like modules, and a __bases__ sequence that provides access to superclasses
* Builtin object has __dict__ attribute provides a dictionary with one key/value pair for every attribute to a namespace
object.

usage of hasattr() and getattr()  -> 
"""

# Instance Versus Class Attributes

"""
* We see that instance attributes attached to the self object shows the objects at the bottom of the inheritance tree 
i.e. what object.__dict__ contains

* We don't see attributes inherited by the instance from classes above it in the tree.Inherited class attributes are
attached to the class only, not copied down to instances.

* To look into the inherited attributes, you can climb the __class__ link to the instance's class, use the __dict__
there to fetch class attributes, and then iterate through the class's __bases__ attribute to climb to even higher
superclass, repeating as necessary.
"""


# Behavior of the Pickle

"""
* When Python pickles a class instance, it records its self instance attribute, along with the name of the class it was
created from and the module where the class lives.
* The upshot of this scheme is that class instances automatically acquires all their class behavior when they are loaded 
in the future.We have to import our classes only to make new instances, not to process existing ones.
* The downside is that classes and their module's files must be importable when as instance is later loaded.
* pickeable classes must be coded at the top level of a module file accessible from a dictionary listed on the sys.path
module search path. 

* Because of the above mentioned complications , some applications choose to pickle simpler objects such as dictionaries
or lists.. 
* The upside -> changes in a class's source code file are automatically picked up when instances of the class are loaded
again, there is often no need to update stored object themselves, since updating their class's behavior changes their
behavior.

"""

# SUMMARIZING NAMESPACES AND SCOPES IN PYTHON
"""
SIMPLE NAMES : GLOBAL UNLESS

* Assignment (X = value) : Makes names local by default , creates or changes the name X in the current local scope,
unless declared global. 

* Reference(X) : Looks for the name X in the current local scope, then any and all enclosing functions, then the 
current global scope, then the built-in scope, per the LEGB rule.
Enclosing classes are not searched : class names are fetched as object attributes instead
 
ATTRIBUTE NAMES : OBJECTS NAMESPACES

* Qualified attribute names refers to attribute of specific objects and obey the rules for modules and classes. For
class and instance objects, the reference rules are augmented to include the inheritance search procedure.

* Assignment(object.X = Value)
Creates or alters the attribute name X in the namespace of the object being qualified, and none other.
Inhertiance-tree climbing happens only on attribute reference, not on attribute assignment.

* Reference(object.X) 
For class-based objects, searches for the attribute name X in the object, then in all accessible classes above it, using
the inheritance search procedure.For nonclass objects such as modules, fetches X from object directly.

"""




