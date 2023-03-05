from sympy.utilities.iterables import multiset_permutations

Buchstaben = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
              "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

allCombinations = list(multiset_permutations(Buchstaben,5))
countB = 0
countE = 0
for combination in allCombinations:
    voc = 0
    kons = 0
    lastletter = "A"
    ordered = True
    for char in combination:
        if (char >= lastletter):
            lastletter = char
        else:
            ordered = False
        if ((char == "A") or (char == "E") or (char == "I") or (char == "O") or (char == "U")):
            voc += 1
        else:
            kons += 1
    if (voc == 2 and kons == 3):
        countB += 1
    if (ordered):
        countE += 1

print(countB)
print(countE)