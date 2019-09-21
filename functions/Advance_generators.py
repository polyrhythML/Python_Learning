# Generators vs Filters

line = "aa bbb cc"

print(''.join(x for x in line.split() if len(x) > 1))       # Outputs : aabbbcc
print(''.join(filter(lambda x : len(x) > 1 , line.split()))) # Outputs : aabbbcc

# filter with map vs generator

print(''.join(map(str.upper, filter(lambda x: len(x) > 1, line.split()))))        # Outputs : AABBBCC
print((''.join(x.upper() for x in line.split() if len(x) > 1)))                   # Outputs : AABBBCC

# With map and filter and comprehension the readability of the output sequence goes down


# Generator functions vs Generator expressions

# Generator function - normal def function which yields a value
# the yielded value is a generator object which has iter method
# and automatically creates a __next__ method
# retains the local scope and code position , where it left from
# resumes from where it left and in case the sequence is finished, raises StopIteration when finishing the producing
# results

# Generator expression
# A comprehension expression enclosed in parenthesis
# It also returns a generator object
# has an __iter__() method and __next__() method


# We can also force all the results at a time, by converting the generator object into list

G = (c * 4 for c in 'SPAM')
print(list(G))              # Outputs : ['SSSS', 'PPPP', 'AAAA', 'MMMM']

# We could have used generator function too for the same, which gives us more statements to work with and more logic
# to be used in the state retention


# Manual iteration

S = (x for x in range(10))
I = iter(S)
print(next(I))                  # Outputs : 0
print(I.__next__())             # Outpus  : 1
print()


# Generator using a function

def gen_func(sequence):
    for x in sequence:
        yield x

S = gen_func([x for x in range(10)])
I = iter(S)
print(I.__next__())
print(next(I))

# Generators are single-Iteration Objects

"""
Generator functions and generator expressions are their own iterators and thus support just one active iteration, 
With builtin types, you can't have multiple iterators of either positioned at different positioned at different
locations in the set of results
"""

G = (c * 4 for c in "SPAM")

I1 = iter(G)
print(next(I1))             # Outputs : SSSS
print(next(I1))             # Outputs : PPPP
I2 = iter(G)
print(next(I2))             # Outpus  : AAAA   second iterator still point to the same position

# Also once your iteration runs completes,all are exhausted... we have to start again

print(next(I2))             # Outputs : MMMM
#print(next(I2))            # Outputs : Stop iteration

I3 = iter(G)
#print(next(I3))              # Outputs : Stop iteration

# Hence we need to make a new iter object again , that G cannot be used anymore
# This is dope, eternal connection , i would say.......

# Lists reflect changes in the active iterators in-place

L = [1, 2, 3, 4]

I1, I2 = iter(L), iter(L)

print(next(I1))                 # Outputs : 1
print(next(I2))                 # Outputs : 1

print(next(I1))                 # Outputs : 2
print(next(I2))                 # Outputs : 2

del(L[2:])

#print(next(I1))                 # Stop iteration
#print(next(I2))                 # Stop iteration

# A single generator's values will be consumed anf exhausted after a single pass

# Builtin types also have their own iterables , behaving in the same manner

# Dictionaries are iterables with iterators that produce keys on each iteration
D = {'a' : 1, 'b' : 2, 'c' : 3}
x = iter(D)
print(next(x))


"""
Note : While built-in type iterables are bound to a specific type of value generation, the concept is similar to
the multipurpose generators we code with expressions and functions.
Iteration contexts like for loops accept any iterable that has the expected methods, whether user-defined 
or built-in..
"""

# os.walk method recursively goes inside the file structure and returns a generator

# Classes also have iterables
# Classes define a special __iter__ method run by iter built-in function, which in turn returns an object having
# a __next__ method() run by the next built-in function


# You cannot process generator objects or scrambled sequences (files, maps , generators) as  the input to a
# generator .Though we can convert those scrambled sequences into sequence
# like the list(generator objects)

# Caller needs to wait until the entire list is complete
# Generator functions retains their local scopes state while active, minimize memory space requirement, and divide
# the work into shorter time slices....

# Difference between the return and yield ...

def permute1(seq):
    if not seq :
        return [seq]
    else :
        res = []
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]
            for x in permute1(rest):
                res.append(seq[i:i+1] + x)
        return res

print(permute1([1, 2, 3]))     # Outputs : [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

def permute2(seq):
    if not seq :
        return [seq]
    else :
        res = []
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]
            for x in permute1(rest):
                yield seq[i:i+1] + x

S = permute2([1, 2, 3])
print(next(S))                # Outputs : [1, 2, 3]

#  The list and generator's results are all same, thought the generator minimizes both the space usage and delays
#  for results. For larger items, the set of permutations is much larger....


# Overall lession : EIBTI --- > Explicit is better than Implicit


# Let's try to emulate zip and map with iteration tool

S1 = "abc"
S2 = "xyz123"
S3 = list(zip(S1, S2))
print(S3)                       # Outputs : [('a', 'x'), ('b', 'y'), ('c', 'z')]

# instead of returning the tuples for all the elements of the list, we can return the elements on demand too ...
# Here comes the power of generators

def mymap(func, *seqs):
    return (func(*args) for args in zip(*seqs))

S = mymap(pow, [1, 2, 3], [1, 2, 3])

print(next(S))          # Outputs : 1
print(next(S))          # Outputs : 4
print(next(S))          # Outputs : 27

# All the variables are localized in the list, dicts, sets, comprehensions
Y = 99
for Y in range(5):      # Be careful with for loops , it can mess up your scopes
    pass
print(Y)                # Outputs : 4

# Both set and dictionary produce all the results at a time ....
# If you mean to produce keys and values upon request, a generator expression is more appropriate


# Generator functions are compiled by python so as to return an iterable generators objects when called.
# That object retains the state and code location between values



