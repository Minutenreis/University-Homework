

def splitIntoSubArrays(A, numberOfSubArrays):
    A.sort()
    Ai = []
    m = len(A) // numberOfSubArrays
    for i in range(numberOfSubArrays):
        Ai.append([])
    for i in range(len(A)):
        j = i//m
        Ai[j].append(A[i])
    return Ai

a1 = [3,1,2,5,4,7,6,8]
a2 = splitIntoSubArrays(a1,2)
for i in range(len(a2)):
    print(a2[i])