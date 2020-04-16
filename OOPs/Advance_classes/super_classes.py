# SUPER CLASSES
"""
Ideally, super should not be used in the cases where we have to inherit from multiple classes.
Rather it's use must be avoided.

Cases where super may still be useful:

• Changing class trees at runtime: When a superclass may be changed at runtime, it’s
not possible to hardcode its name in a call expression, but it is possible to dispatch
calls via super .
On the other hand, this case is extremely rare in Python programming, and other
techniques can often be used in this context as well.

• Cooperative multiple inheritance method dispatch: When multiple inheritance trees
must dispatch to the same-named method in multiple classes, super can provide a
protocol for orderly call routing.
On the other hand, the class tree must rely upon the ordering of classes by the
MRO—a complex tool in its own right that is artificial to the problem a program
is meant to address—and must be coded or augmented to use super in each version
of the method in the tree to be effective. Such dispatch can also often be imple-
mented in other ways (e.g., via instance state).

"""


class C:

    def __init__(self):
        print("this is C")

    def act(self):
        print("C")


class D(C):
    def __init__(self):
        super().__init__()
        print("This is D")


    def act(self):
        print("D")

### CHANGING THE CLASS TREE AT RUN-TIME
############### RUN TIME CLASS CHANGES AND SUPER ###############

class X:
    def m(self):
        print("This is X")


class Y:
    def m(self):
        print("This is Y")


class Z(X):
    def m(self):
        #super().m()
        Z.__bases__[0].m(self)


if __name__ == "__main__":

    X = D()
    X.act()

    obj1 = Z()
    obj1.m()        # Outputs : This is X

    # Change the base class of the Z
    Z.__bases__ = (Y, )
    obj1.m()        # Outputs : This is Y
