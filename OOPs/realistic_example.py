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
* Behavior methods - encapsulatinf logic in a class's methods 
* Operating overloading - providing behavior for built-in operations
* Customizing behavior - redefining subclasses 
* Customizing constructors - adding initialization logic to superclass steps 
 
"""

# USING INTROSPECTION TOOL !!


