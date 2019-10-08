# Comparison operators can also be overloaded
"""
* In the iteration domain, classes can implement in membership operator as n iteration, using either the __iter__ or
__getitem__ methods.To support more specific membership, though, classes may code a __contains__ method when present,
this method is preferred over __iter__, which is preferred over __getitem__.

"""


class Iters:
    def __init__(self, value):
        self.data = value

    def __getitem__(self, i):
        print("get[%s]:"%i, end="")
        return self.data[i]

    def __iter__(self):
        print("iter=>", end="")
        self.ix = 0
        return self

    def __next__(self):
        print("next:", end="")
        if self.ix == len(self.data):
            raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item

    def __contains__(self, x):
        print("contains: ", end="")
        return x in self.data


class Iters_multi_iterator:
    def __init__(self, value):
        self.data = value

    def __getitem__(self, i):
        print("get[%s]:" % i, end="")
        return self.data[i]

    def __iter__(self):                         # Preferred over iteration
        print("iter=> next:", end="")           # Allows multiple active iterators
        for x in self.data:                     # no __next__ to alias to next
            yield x
            print("next:", end="")

    def __contains__(self, x):
        print("contains: ", end="")
        return x in self.data


if __name__ == "__main__":
    X = Iters([1, 2, 3, 4, 5])
    print(3 in X)                   # __contains__ is called
    for i in X:
        print(i, end="|")           # __iter__ and __next__ is called
    print()
    print([i **2 for i in X])       # __iter__ and __next__ is called
    print(list(map(bin, X)))        # __iter__ and __next__ is called
    I = iter(X)
    while True:
        try:
            print(next(I), end="@") # __iter__ and __next__ is called
        except StopIteration:
            break

    """
    Output:
    iter=>next:1|next:2|next:3|next:4|next:5|next:
    iter=>next:next:next:next:next:next:[1, 4, 9, 16, 25]
    iter=>next:next:next:next:next:next:['0b1', '0b10', '0b11', '0b100', '0b101']
    iter=>next:1@next:2@next:3@next:4@next:5@next:(base)
    """

    X = Iters_multi_iterator([1, 2, 3, 4, 5])
    print(3 in X)                   # __contains__ is called
    for i in X:
        print(i, end="|")           # __iter__ and __next__ is called
    print()
    print([i **2 for i in X])       # __iter__ and __next__ is called
    print(list(map(bin, X)))        # __iter__ and __next__ is called
    I = iter(X)
    while True:
        try:
            print(next(I), end="@") # __iter__ and __next__ is called
        except StopIteration:
            break

    # If you comment out __contains__, the membership test is routed to __iter__ method, and if both of them are
    # commented out then membership is routed to __getitem__ method.(Test for yourself to see the output)
