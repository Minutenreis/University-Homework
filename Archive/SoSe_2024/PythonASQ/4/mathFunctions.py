import math

def potenz(x:float,n:int) -> float:
    if n == 0:
        return 1
    if n < 1:
        return 1 / potenz(x, -n)
    # square and multiply
    if n % 2 == 0:
        return potenz(x * x, n // 2)
    else:
        return x * potenz(x * x, n // 2)

def potenz_iter(x:float,n:int) -> float:
    if n < 0:
        x = 1 / x
        n = -n
    if n == 0:
        return 1
    y = 1
    # square and multiply
    while n > 1:
        if n % 2 != 0:
            y *= x
            n -= 1
        x *= x
        n //= 2
    return x * y

def fakultät(x: int) -> int:
    if x < 0:
        raise ValueError("Fakultät ist nur für positive Zahlen definiert")
    if x == 0:
        return 1
    return x * fakultät(x - 1)

def sin(x: float) -> float:
    sum = 0
    n = 0
    lastSum = -1
    while abs(sum - lastSum) > 1e-10:
        lastSum = sum
        sum += potenz(-1, n) * potenz(x, 2 * n+1) / fakultät(2 * n+1)
        n += 1
    return round(sum,10)