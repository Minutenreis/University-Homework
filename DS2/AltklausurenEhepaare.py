from sympy.utilities.iterables import multiset_permutations

Ehepaare = [1,2,3,4,5,6,7,8] #1,2 Ehepaar, 3,4 Ehepaar, 5,6 Ehepaar, 7,8 Ehepaar
Kombinationen = list(multiset_permutations(Ehepaare))
count = 0
for comb in Kombinationen:
    Ehe12 = False
    Ehe34 = False
    last = comb[7]
    for i in comb:
        if (((i == 2) & (last == 1)) | ((i == 1) & (last == 2))):
            Ehe12 = True
        if (((i == 4) & (last == 3)) | ((i == 3) & (last == 4))):
            Ehe34 = True
        last = i
    if (Ehe12 & Ehe34):
        count += 1
print(count)