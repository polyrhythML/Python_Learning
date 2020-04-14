# DECORATORS

"""
* Decoration is a way to run extra processing steps at function and class definition time with explicit syntax.

    • Function decorators—the initial entry in this set, added in Python 2.4—augment
        function definitions. They specify special operation modes for both simple func-
        tions and classes’ methods by wrapping them in an extra layer of logic implemented
        as another function, usually called a metafunction.
    • Class decorators—a later extension, added in Python 2.6 and 3.0—augment class
        definitions. They do the same for classes, adding support for management of whole
        objects and their interfaces. Though perhaps simpler, they often overlap in roles
        with metaclasses.

* Example see the static_method.py file for reference
 class C:                               class C:
    @staticmethod                           def meth():
   def meth():                              meth = staticmethod(meth)
    pass

* Decorator rebinds the method name to the decorator's result. The net effect is that calling the method function's
name later actually triggers the result of it's staticmethod.
"""

class Methods(object):

    def imeth(self, x):     # object needed in 2.X for property setters
        print([self, x])    # Normal instance method: passed a self

    @staticmethod
    def smeth(x):
        print([x])          # Static: no instance passed

    @classmethod
    def cmeth(cls, x):
        print([cls, x])     # Class: gets class, not instance

    @property               # Property: computed on fetch
    def name(self):
        return 'Bob ' + self.__class__.__name__


if __name__ == "__main__":

    obj = Methods()
    print(obj.imeth(1))
    print(obj.smeth(2))
    print(obj.cmeth(3))
    print(obj.name)
