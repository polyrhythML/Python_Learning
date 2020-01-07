# OOPs CODE DESIGN PATTERN IN PYTHON

"""
Unlike other programming languages where the term polymorphism is related to the operator overloading by the use of the
signature of the function arguments, Python doesnot support type declaration therefore here the polymorphism is based on
the object interfaces and not types.

"""

def example_method(x, y):
    print(x+y)


def example_method(x, y):
    print(x*y)


## OOPs and Inheritance

"""
Inheritance is a way to specify set membership, a class defines a set of properties that may be inherited and customized
by more specific sets
Example of Pizze shop 

base class - Employee 
sub classes - server, chef 
sub - sub class - Pizzarobot a kind of a chef, which is a kind of an Employee.
In OOP terms, we call these relationships "is-a" links: a robot is a chef.
"""
# Let's build our employee class


class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    def giveRaise(self, percent):
        self.salary = self.salary + (self.salary * percent)

    def work(self):
        print(self.name, "does stuff")

    def __repr__(self):
        return "<Employee: name={}, salary={}>".format(self.name, self.salary)


class Chef(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 50000)

    def work(self):
        print(self.name, "makes food")


class Server(Employee):
    def __init__(self, name):
        Employee.__init__(self, name)

    def work(self):
        print(self.name, "Interacts with the customer")


class PizzaRobot(Chef):
    def __init__(self, name):
        Chef.__init__(self, name)

    def work(self):
        print(self.name, "makes pizza")


################ OOPs and Composition ##############################
"""

* Composition involves embedding other objects in a container object and activating them to implement container
methods.
* Rather than set membership, composition has to do with components -- parts of a whole.
* Essentially, a "composition" simply refers to a collection of embedded objects. The composite class generally
provides an interface all its own and implements it by directing the embedded objects.

# Pizza shop is a composite object and has an oven and it has employees, servers and chefs

Classes - Noun
methods - Verbs 
"""


class Customer:
    def __init__(self, name):
        self.name = name

    def order(self, server):
        print(self.name, "orders from", server)

    def pay(self, server):
        print(self.name, "pay for item to", server)


class Oven:
    def bake(self):
        print("oven bakes")


class PizzaShop:
    def __init__(self):
        self.server = Server('Pat')
        self.chef = PizzaRobot('Bob')
        self.oven = Oven()

    def order(self, name):
        customer = Customer(name)       # Activate other objects
        customer.order(self.server)     # Customer orders from server
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)


################################# OOPs and Delegation ################################

"""
Delegation is a special form of composition, with a single embedded object managed by a wrapper class that retains most
or all of the embedded object's interface.
"""

class Wrapper:
    def __init__(self, object):
        self.wrapped = object

    def __getattr__(self, attrname):
        print("Trace : " + attrname)
        return getattr(self.wrapped, attrname)

################## Pseudoprivate Class Attributes ####################

"""
* There are no private objects in python and we usually define a private object in python using _X as the convention.
* Python doesnot support mangling, i.e. localizing some names in classes. Mangled names are sometimes misleading called
"""
####### CASE 1 ######


class C1:

    def meth1(self):
        self.X = 88

    def meth2(self):
        print(self.X)


class C2:

    def metha(self):
        self.X = 99

    def methb(self):
        print(self.X)


class C3(C1, C2):
    pass
# When you instantiate this class I = C3() ---> I.X ---> self.X will depend on which class assigned it last.
#  If you had metha(self): self.X as self.__X then it becomes _C1__X

##### CASE 2 #####


class Super:
    def method(self): pass


class Tool:
    def __method(self): pass        # __method becomes _Tool__method internally

    def other(self): self.__method()    # internal __method called


class Sub1(Tool, Super):
    def action(self):
        self.method()               # Here the method() is from super and not Tool as per the rule of inheritance
                                    # lookup left to right


class Sub2(Tool):
    def __init__(self):
        self.method() == 99         # Doesnot break Tool.__method, this means... Tool class's method is called


########################## BOUND AND UNBOUND METHODS #########################

"""
bound methods : associated to a class 
Unbound methods : do not require an instance to called 

"""

class Selfless:

    def __init__(self, data):
        self.data = data

    def selfless(arg1, arg2):               # Unbounded function
        return arg1 + arg2

    def normal(self, arg1, arg2):           # bounded function
        return self.data + arg1 + arg2

# X = Selfless(2)
# X.normal(3, 4)   ------> perfectly normal call to the normal function
# Selfless.normal(X, 3, 4) -------> all cool
# Selfless.selfless(3, 4) ------> works in 3.x but fails in 2.x
# Below 2 cases fails in both 3.X and 2.X

# X.selfless(3, 4) ----> 2 positional arguments expected but 3 were given, self as first one
# Selfless.normal(3, 4) ----> one argument missing , since first argument place it considers it as self

############### CLASSES GENERIC OBJECT FACTORIES ############

"""

* Class base designs require objects to be created in response to conditions that can't be predicted when a program is 
written.

* Passing the classes to the functions that generate arbitrary kinds of objects such functions are called the factories
in OOPs design circles.

Why factories ?

* Factory style functions come in handy here because they would allow us to fetch and pass in classes that cannot be har
coded in our program ahead of time. Indeed, those classes might not even have existed at all when wrote our code.
* The factory function proves more useful in the presence of unknown arguments lists, however, and the general factory
coding pattern can improve the code's flexibility. 
"""

############# MULTIPLE INHERITANCE ######################

"""
* When search for an attributem Python's inheritance search traverses all the superclassses in the class header from 
left to right until a match is found.But if superclasses have their own super classes then , the larger class tree
structure becomes more complex.

* In classic classes, the attribute search in all cases proceeds depth-first all the way to the top of the inheritance
tree, and then from left to right. This order is usually called DFLR, for its depth-first, left-to-right path.

* The new method is called MRO, method resolution order. The attribute search is usually as before but in a diamond
patterns across by tree levels before moving up , in a more breadth-first fashion.

* Multiple inheritance is a good for modelling objects that belong to more than one set.Multiple inheritance also allows
classes to function as general package of mixable attributes.

* Resolve same name conflict : 
    
    * Default : By default, inheritance chooses the first occurence of an attribute it finds when an attribute is 
    referenced normally- by self.method(), for example. In this mode, Python choose the lowest and the leftmost in 
    classic classes, and in nondiamond patterns in all classes, new style classes may choose an option to the right
    before once above the diamonds.
    
    * Explicit : In some class models, you may sometimes need to select an attribute explicitly by referencing it 
    through its class name with superclass.method(self) for the instance.
"""




if __name__ == "__main__":
    example_method(2, 3)

    ################# OOPs and Inheritance #######################

    # Output : 6 (last method call is invoked)
    bob = PizzaRobot("bob")
    print(bob)
    bob.work()
    bob.giveRaise(0.20)
    print(bob)
    # Outputs :
    """
    Outputs : 
    6
    <Employee: name=bob, salary=50000>
    bob makes pizza
    <Employee: name=bob, salary=60000.0>
    """

    for klass in Employee, Chef, Server, PizzaRobot:
        obj = klass(klass.__name__)
        obj.work()
    """
    Outputs : 
    Employee does stuff
    Chef makes food
    Server Interacts with the customer
    PizzaRobot makes pizza
    """

    #################### OOPs and Composition ########################

    scene = PizzaShop()
    scene.order("Homer")
    print("...")
    scene.order("Shaggy")

    ##################### OOPs and Delegation #########################

    x = Wrapper([1, 2, 3, 4])
    x.append(4)
    x.wrapped

    #################### Classes as the Object factories ################





