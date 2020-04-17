# Classes are Mutable objects
"""
* The class attributes are shared by all instances if a class attribute
a mutable object, changing that object in place from any instance impacts all
instances at once.

Miscellaneous Class Gotchas

* Choose per-instance or class storage wisely :
On a similar note, be careful when you decide whether an attribute should be stored
on a class or its instances: the former is shared by all instances, and the latter will differ
per instance. This can be a crucial design issue in practice. In a GUI program, for
instance, if you want information to be shared by all of the window class objects your
application will create (e.g., the last directory used for a Save operation, or an already
entered password), it must be stored as class-level data; if stored in the instance as
self attributes, it will vary per window or be missing entirely when looked up by in-
heritance.

* You usually want to call superclass constructors :
Remember that Python runs only one __init__ constructor method when an instance
is made—the lowest in the class inheritance tree. It does not automatically run the
constructors of all superclasses higher up. Because constructors normally perform re-
quired startup work, you’ll usually need to run a superclass constructor from a subclass
constructor—using a manual call through the superclass’s name (or super ), passing
along whatever arguments are required—unless you mean to replace the super’s con-
structor altogether, or the superclass doesn’t have or inherit a constructor at all.

* Classes that use the __getattr__ operator overloading method to delegate attribute
fetches to wrapped objects may fail in Python 3.X (and 2.X when new-style classes are used)
unless operator overloading methods are redefined in the wrapper class.
The names of operator overloading methods implicitly fetched by built-in
operations are not routed through generic attribute-interception methods.


"""

class A:
    name = "trippo"


X = A()
X.name = "trippy"
print(X.name)

A.name = "trippyio"
Y = A()

print(Y.name)


class C:
    class_attr = []
    def __init__(self):
        self.obj_attr = []


x = C()
y = C()
print(x.class_attr, x.obj_attr)         # Output: [] []
print(y.class_attr, y.obj_attr)         # Output: [] []

x.class_attr.append("trippy")
x.obj_attr.append("code")

print(x.class_attr, x.obj_attr)         # Output : ['trippy'] ['code']
print(y.class_attr, y.obj_attr)         # Output : ['trippy'] []

# Scopes of classes enclosed in the methods

"""
* Method defs cannot see the local scope of the enclosing class; they can 
see only the local scopes of enclosing defs. That’s why methods must go through 
the self instance or the class name to reference methods and other attributes
defined in the enclosing class statement.

"""

def generate():

    class Spam:             # Spam is a name generate's local scope
        count = 1
        def method(self):
            print(Spam.count)   # Visible in generate's scope, per LEGB
        return Spam()

# We can restructure the above code to have Spam class in the global scope and
# then call it in the generate function

def generate():
    return Spam()

class Spam:
    count = 1
    def method(self):
        print(Spam.count)

""""
WHY OOPs

* Code reuse
This one’s easy (and is the main reason for using OOP). By supporting inheritance,
classes allow you to program by customization instead of starting each project from
scratch.

* Encapsulation
Wrapping up implementation details behind object interfaces insulates users of a
class from code changes.

* Structure
Classes provide new local scopes, which minimizes name clashes. They also pro-
vide a natural place to write and look for implementation code, and to manage
object state.

* Maintenance
Classes naturally promote code factoring, which allows us to minimize redun-
dancy. Thanks both to the structure and code reuse support of classes, usually only
one copy of the code needs to be changed.

* Consistency
Classes and inheritance allow you to implement common interfaces, and hence
create a common look and feel in your code; this eases debugging, comprehension,
and maintenance.

* Polymorphism
This is more a property of OOP than a reason for using it, but by supporting code
generality, polymorphism makes code more flexible and widely applicable, and
hence more reusable.


"""