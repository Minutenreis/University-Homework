from sympy.utilities.iterables import multiset_permutations

options = []
for i in range(10):
    options.append(1)
    options.append(2)
    options.append(3)
for i in range(9):
    options.append(4)

array = list(multiset_permutations(options,10))
print(len(array))