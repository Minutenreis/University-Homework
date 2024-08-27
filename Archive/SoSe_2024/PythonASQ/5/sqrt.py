# why is this not the intended solution?
def sqrtIteration(x, n=10):
    z = 1
    for _ in range(n):
        z = 0.5 * (z + x/z)
    return z

# if we already do tail recursion, we might as well do it iteratively
def sqrtTailRecursion(x, n = 10, z = 1):
    if n <= 0:
        return z
    return sqrtTailRecursion(x, n-1, 0.5*(z + x/z))

# tree recursion is unnecessarily slow
def sqrtTreeRecursion(x, n=10):
    if n <= 0:
        return 1
    return 0.5 * (sqrtTreeRecursion(x, n-1) + x / sqrtTreeRecursion(x, n-1))

print("sqrtIteration, sqrtTailRecursion, sqrtTreeRecurion")
print(sqrtIteration(2), sqrtTailRecursion(2), sqrtTreeRecursion(2))
print(sqrtIteration(4),sqrtTailRecursion(4), sqrtTreeRecursion(4))
print(sqrtIteration(9),sqrtTailRecursion(9), sqrtTreeRecursion(9))
print(sqrtIteration(0.25),sqrtTailRecursion(0.25), sqrtTreeRecursion(0.25))
print(sqrtIteration(0),sqrtTailRecursion(0), sqrtTreeRecursion(0))