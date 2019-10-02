import namespaces_scopes

X = 66
print(X)                        # Outputs : 66
print(namespaces_scopes.X)      # Outputs : 11

namespaces_scopes.f()           # Outputs : 11
namespaces_scopes.g()           # Outputs : 22
print(namespaces_scopes.C.X)    # Outputs : 33


I = namespaces_scopes.C()
print(I.X)                      # Outputs : 33
I.m()
print(I.X)                      # Outputs : 55



###############################################################################

X = 1

def nester():
    print(X)                        # Output : 1
    class C:
        print(X)                    # Outputs : 1
        def method1(self):
            print(X)                # Outputs :1
        def method2(self):
            X = 3
            print(X)                # Output : 3
    I = C()
    I.method1()
    I.method2()

print("Let's get the output")
print(X)
nester()
print("-"*40)

####################################################################################

X = 1


def nester():
    X = 2
    print(X)                    # Outputs : 2

    class C:
        print(X)                # Outputs : 2

        def method1(self):
            print(X)            # Outputs : 2

        def method2(self):
            X = 3
            print(X)            # Outputs : 3
    I = C()
    I.method1()
    I.method2()

nester()
print("-"*40)


##########################################################################################

X = 1

def nester():
    X = 2
    print(X)                 # Outputs : 2

    class C:
        X = 3
        print(X)             # Outputs : 3

        def method1(self):
            print(X)         # Outputs : 2   -------> In enclosing def
            print(self.X)    # Outputs : 3

        def method2(self):
            X = 4
            print(X)         # Outputs : 4
            self.X = 5
            print(self.X)    # Outputs : 5
    I = C()
    I.method1()
    I.method2()

print(X)
nester()
print("-"*40)


################################ DICTIONARIES REVIEW ##########################################

class Super:
    def hello(self):
        self.data1 = "spam"

class Sub(Super):
    def hola(self):
        self.data2 = "eggs"


X = Sub()
print(X.__dict__)           # empty dictionary , since no variables initialized as there is no constructor
print(X.__class__)          # object of class Sub, <class '__main__.Sub'>
print(Sub.__bases__)        # tuple of bases classes (<class '__main__.Super'>,)
print(Super.__bases__)      # since there is no base class

Y = Sub()
X.hello()
print(X.__dict__)           # Outputs : {'data1': 'spam'}

X.hola()
print(X.__dict__)           # Outputs : {'data1': 'spam', 'data2': 'eggs'}

print(list(Sub.__dict__.keys()))        # Outputs : ['__module__', 'hola', '__doc__']
print(list(Super.__dict__.keys()))      # Outputs : ['__module__', 'hello', '__dict__', '__weakref__', '__doc__']



