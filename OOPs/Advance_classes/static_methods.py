# STATIC and CLASS METHODS

"""
* Static methods are simply the instance-less functions inside a class.
* Class methods are passed a class instead of an instance.
* In Python 3.X, a staticmethod declaration is not required for instance-less methods called only
through a class name, but is still required if such methods are called through instances.

* Why special methods ?
    Some functions required to keep track of the class's meta data i.e. the number of instances associated with the
    class. List of all class objects in the memory. This type of information and processing are associated with the
    class rather than it's instances.

    Static methods - simple functions, with no self argument that are nested in a class and are designed to work on
    class attributes. They keep track of the information that spans all instances, rather than providing behaviour for
    instances.

    Class methods - methods of class passed a class object in their first argument instead of an instance, regardless
    of whether they are called through an instance or a class.


* Statics in 2.X and 3.X
    • Both Python 2.X and 3.X produce a bound method when a method is fetched
    through an instance.
    • In Python 2.X, fetching a method from a class produces an unbound method, which
    cannot be called without manually passing an instance.
    • In Python 3.X, fetching a method from a class produces a simple function, which
    can be called normally with no instance present

* In other words, Python 2.X class methods always require an instance to be passed in,
whether they are called through an instance or a class. By contrast, in Python 3.X we
are required to pass an instance to a method only if the method expects one—methods
that do not include an instance argument can be called through the class without pass-
ing an instance.
    • In Python 2.X, we must always declare a method as static in order to call it without
        an instance, whether it is called through a class or an instance.
    • In Python 3.X, we need not declare such methods as static if they will be called
        through a class only, but we must do so in order to call them through an instance.

"""


class Spam:

    num_Instances = 0

    def __init__(self):
        Spam.num_Instances = Spam.num_Instances + 1

    def printNumInstances():
        print("Number of instances created: %s" % Spam.num_Instances)

    printNumInstances = staticmethod(printNumInstances)


class Sub(Spam):

    def printNumInstances():
        print("Extra stuff ...")
        Spam.printNumInstances()
    printNumInstances = staticmethod(printNumInstances)

    def clsprintNumInstances(cls):
        Spam.printNumInstances(cls)

    printNumInstances = classmethod(printNumInstances)


class Others(Spam):
    pass


if __name__ == "__main__" :

    a = Spam()
    b = Spam()
    c = Spam()

    # Access static method using only the Class with dot operator.
    print(Spam.printNumInstances())     # Output : 3

    # Can't access the static method with class's object
    #print(a.printNumInstances())        # Output :TypeError: printNumInstances() takes 0 positional arguments
                                        # but 1 was given

    d = Sub()
    print(d.printNumInstances())        # Output : 4

    e = Others()
    print(e.printNumInstances())        # Output : 5
