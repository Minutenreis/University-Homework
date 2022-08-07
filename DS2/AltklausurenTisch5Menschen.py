from sympy.utilities.iterables import multiset_permutations
def isValid(comb: list):
    last = comb[len(comb)-1]
    for i in comb:
        if(i != 0  and last != 0):
            return False
        last = i
    return True

guests = [1,2,3,4,5,0,0,0,0,0,0,0]

combinations = list(multiset_permutations(guests))
count = 0
for comb in combinations:
    if (isValid(comb)):
        count += 1
print(count)


        