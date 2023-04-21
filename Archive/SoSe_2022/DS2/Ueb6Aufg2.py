from sympy.utilities.iterables import multiset_permutations

def arrayIncludesNoDoubles(array: list) -> bool:
    for i in range(len(array)-1):
        if (array[i] == array[i+1]):
            return False
    return True

array = list(multiset_permutations([1,1,1,2,2,3,3,4,5,6]))
count = 0
for element in array:
    if(arrayIncludesNoDoubles(element)):
        count+= 1
print(count)

