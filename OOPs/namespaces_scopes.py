X = 11


def f():
    print(X)


def g():
    X = 22
    print(X)


class C:

    X = 33

    def m(self):
        X = 44
        self.X = 55


if __name__=="__main__":
    print(X)    # Outputs : 11
    f()         # Outputs : 11
    g()         # Outputs : 22
    print(X)    # Outputs : 11

    obj = C()
    print(obj.X)    # Outputs : 33

    obj.m()
    print(obj.X)    # Outputs : 55
    print(C.X)      # Outputs : 33
#    print(C.m.X)    # Not accessible in the method call


