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


SUMMARY

* Perhaps the chief problem of this role, though, is the role itself—same-named method
dispatch in multiple inheritance trees is relatively rare in real Python programs, and
obscure enough to have generated both much controversy and much misunderstanding
surrounding this role. People don’t use Python the same way they use C++, Java, or
Dylan, and lessons from other such languages do not necessarily apply

*

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

############### CHANGING THE CLASS TREE AT RUN-TIME ############s
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


############### Cooperative Multiple Inheritance Method Dispatch ############

# Example 1

class A1:
    def __init__(self):
        print("This is A1")


class B1(A1):
    def __init__(self):
        print("This is B1")
        A1.__init__(self)


class C1(A1):
    def __init__(self):
        print("This is C1")
        A1.__init__(self)


class D1(B1, C1):
    def __init__(self):
        B1.__init__(self)
        C1.__init__(self)

# Example 2

class A2:
    def __init__(self):
        print("This is A1")


class B2(A2):
    def __init__(self):
        print("This is B1")
        super().__init__()


class C2(A2):
    def __init__(self):
        print("This is C1")
        super().__init__()


class D2(B2, C2):
    pass



if __name__ == "__main__":

    X = D()
    X.act()

    obj1 = Z()
    obj1.m()        # Outputs : This is X

    # Change the base class of the Z
    Z.__bases__ = (Y, )
    obj1.m()        # Outputs : This is Y

    X1 = D1()
    print(D1.__mro__)
    # Output : (<class '__main__.D1'>, <class '__main__.B1'>, <class '__main__.C1'>,
    # <class '__main__.A1'>, <class 'object'>)

    X2 = D2()
    print(D2.__mro__)
    # Output : (<class '__main__.D2'>, <class '__main__.B2'>, <class '__main__.C2'>,
    # <class '__main__.A2'>, <class 'object'>)

