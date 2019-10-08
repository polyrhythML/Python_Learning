class SkipObject:
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def __iter__(self):
        return SkipIterator(self.wrapped)


class SkipIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.offset = 0

    def __next__(self):
        if self.offset >= len(self.wrapped):
            raise StopIteration
        else:
            item = self.wrapped[self.offset]
            self.offset += 2
            return item


if __name__ == "__main__":

    alpha = "abcdef"
    skipper = SkipObject(alpha)
    I = iter(skipper)
    print(next(I), next(I), next(I))        # Outputs : a c e

    # Here we have only one skip object with multiple instances of the iterator object
    for x in skipper:
        for y in skipper:
            print(x + y, end=" ")           # Outputs : aa ac ae ca cc ce ea ec ee

    # Another way to achieve the same result

    S = "abcdef"
    for x in S[::2]:
        for y in S[::2]:
            print(x+y, end=" ")
    """
    Above is not same as the skipper object that we have created.Slice creates a new object in every iteration.
    Also, it stores the result list all at once in the memory.Unlike iterables which store one value at a time.
    """