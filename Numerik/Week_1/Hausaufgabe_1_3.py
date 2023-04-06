import numpy as np


def f(x): return 2**x - 4 * x - 1


def g(x): return x**3 - x


def getInterval(f, a: np.double, b: np.double):
    while(b-a > np.double(0.065)):
        c = (a+b)/2
        if(f(a) > 0 and f(c) < 0 or f(a) < 0 and f(c) > 0):
            b = c
        else:
            a = c
    print("Interval: [", a, ",", b, "]")
    return


a = np.double(4)
b = np.double(4.5)

getInterval(f, a, b)
