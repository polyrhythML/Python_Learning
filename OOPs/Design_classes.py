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


