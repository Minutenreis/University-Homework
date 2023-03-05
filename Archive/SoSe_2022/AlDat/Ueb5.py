def getMedian(C: list, CIndex: int, n: int) -> float:
    if (n % 2 == 0):
        return (C[CIndex + n//2 - 1] + C[CIndex + n//2])/2
    else:
        return C[CIndex + n//2]


def median(A: list, AIndex: int, B: list, BIndex: int, n: int) -> float:
    if(n == 0):
        return 0
    if(n == 1):
        return (A[AIndex] + B[BIndex])/2
    if(n == 2):
        C = [A[AIndex], A[AIndex+1], B[BIndex], B[BIndex+1]]
        C.sort()
        return getMedian(C,0, 4)

    m1 = getMedian(A, AIndex, n)
    m2 = getMedian(B, BIndex, n)

    if(m1 == m2):
        return m1
    if (m1 < m2):
        return median(A, AIndex+n//2, B, BIndex, n - n//2)
    else:
        return median(A, AIndex, B, BIndex + n//2, n - n//2)


A = [1,3,6,12,14]
B = [2,5,7,8,10]
print(median(A, 0, B, 0, len(A)))
