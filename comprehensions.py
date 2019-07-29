# Let's study some advanced comprehensions and generators

# Comprehensions apply an arbitrary expression to the items in an iterable instead of a function

# List compreshension vs Map

example_list = "spam"
res = []
for x in example_list:
    res.append(ord(x))
print(res)                              # outputs : [115, 112, 97, 109]

# res created using map, it maps over an iterable
res = list(map(ord, example_list))
print(res)                              # outputs : [115, 112, 97, 109]


# using list comprehension now

res =[ord(x) for x in example_list]
print(res)                              # outputs : [115, 112, 97, 109]


# We can have an expression applied over an iterable with map by using lambda inline function

res = list(map((lambda x : x**2), range(10)))

# General rule :
# Expression --> something that evaluates something --- > 2+2, 2*2
# Statement  --> doesnot return any value --- > for i in range(10), while ( i < 10 )



# List Comprehension with if clause analogous to filter statement

# filter in action :

rec = list(filter((lambda x : x % 2 == 0), range(5)))
print(rec)                          # outputs : [0, 2, 4]

# Same list comprehension

rec = [ x for x in range(5) if x % 2 ==0 ]
print(rec)                          # Outputs : [0, 2, 4]


# Nested list comprehensions are also there with if clauses

rec = [x + y + z for x in 'spam' if x in "sm" for y in "SPAM" if y in ('P', 'A')
        for z in '123' if z > '1']
print(rec)                          # Outputs :['sP2', 'sP3', 'sA2', 'sA3', 'mP2', 'mP3', 'mA2', 'mA3']

# List comprehensions and Matrices , better love story than Twilight


M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
N = [[2, 2, 2],
     [3, 3, 3],
     [4, 4, 4]]

print(M[1])                             # Outputs : [4, 5, 6]
print(N[1][2])                          # Outputs : 3


# Accessing a column
rec = [row[1] for row in M ]            # Column 2
print(rec)

# Using offset
# Accessing 2nd element of each row or basically the 2nd column
rec = [M[row][1] for row in (0, 1, 2)]
print(rec)


# Diagonal access
diagonal_list = [M[i][i] for i in range(len(M))]
print(diagonal_list)                                # Outputs : [1, 5, 9]

# We cannot change lists in place using list comprehensions , but we can create a new list out of the
# existing list

L = [[1, 2, 3],
    [4, 5, 6]]

# Changing list in place
for i in range(len(L)):
    for j in range(len(L[i])):
        L[i][j] += 10
print(L)                        # Outputs : [[11, 12, 13], [14, 15, 16]]

# creating a list by using existing list

changed_list = [L[i][j]*2 for i in range(len(L)) for j in range(len(L[i]))]
print(changed_list)             # Outputs : [22, 24, 26, 28, 30, 32]

# Check whether changed_list is L or not
print(L is changed_list)        # Outputs : False


L = [[1, 2, 3],
     [4, 5, 6]]

rec = [[col + 10 for col in row] for row in M]
print(rec)                      # Outputs : [[11, 12, 13], [14, 15, 16], [17, 18, 19]]


# Equivalent for loop :
res = []
for row in M :
    for col in row :
        res.append(col + 10)    # Outputs : [[11, 12, 13], [14, 15, 16], [17, 18, 19]]
print(rec)


# Matrix multiplication
M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
N = [[2, 2, 2],
     [3, 3, 3],
     [4, 4, 4]]
# make sure to check N X M rule to be valid, before you apply transformation
# (matrix multiply is essentially a linear transformation)
multi_matrix = [M[row][col]*N[row][col] for row in range(3) for col in range(3)]

print(multi_matrix)                     # Outputs : [2, 4, 6, 12, 15, 18, 28, 32, 36]

# List comprehension a kiss story !!

"""
List comprehension can quickly become, well, incomprehensible, especially when nested.Some programming tasks are
inherently complex, we can't sugarcoat them to make them any simpler than thet are.
Complicated comprehensions can lead to loss in readablility of the code, which should be your one of the prime 
focus

* Still for loops are recommended for the sake of the simplicity they provide
"""

"""
Let's take about some speed -----> Fast N Furious 

* Maps can be twice as fast as equivalent for loops
* List comprehensions are often faster than map calls.
* List comprehensions and map run at C language speed inside the interpreter, which is often much faster that 
stepping through Python for loop bytecode within PVM
"""














