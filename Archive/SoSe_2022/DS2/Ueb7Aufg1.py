arrayTwoPotency = []
arrayThreePotency = []
arrayFourPotency = []
value = 1
while(value**2 <=100000):
    arrayTwoPotency.append(value**2)
    value = value+1

value = 1
while(value**3 <=100000):
    arrayThreePotency.append(value**3)
    value = value+1

value = 1
while(value**4 <=100000):
    arrayFourPotency.append(value**4)
    value = value+1

mergedarray = []

for elem in arrayTwoPotency:
    mergedarray.append(elem)

for elem in arrayThreePotency:
    if elem not in mergedarray:
        mergedarray.append(elem)

for elem in arrayFourPotency:
    if elem not in mergedarray:
        mergedarray.append(elem)

print(arrayTwoPotency)
print(len(arrayTwoPotency))
print(len(arrayThreePotency))
print(len(arrayFourPotency))
print(len(mergedarray))