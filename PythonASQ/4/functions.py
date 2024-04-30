def f(x): return x**2+2
def g(x,y): return (x-y)/(x+y)
def fib(n):
    a,b = 0,1
    for _ in range(n):
        a,b = b,a+b
    return a
def ulam(a):
    while a != 1:
        if a % 2 == 0:
            a = a // 2
        else:
            a = 3 * a + 1
        print(a)
    return a


n=1000000
def test(zahl: int):
    print(id(zahl))
    zahl = zahl // 2
    print(id(zahl))
print(id(n))
test(n)
print(n)
# https://stackoverflow.com/a/986145