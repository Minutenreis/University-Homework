import numpy as np
import random
import matplotlib.pyplot as plt


def f(x): return 1+x**3-3*x**2


def f1(x): return 3*x**2-6*x


def phi(x): return x-f(x)/f1(x)


def phi1(x, xalt): return x-f(x)/((f(x)-f(xalt))/(x-xalt))


def genIteration(x):
    xalt = x-1
    xrange = [x]
    i = 0
    while (i < 20 and np.abs(x-xalt) > 1e-7):
        xalt = x
        x = phi(x)
        xrange.append(x)
        i += 1
    return xrange


def genIterationApprox(x, xalt):
    xrange = [x]
    i = 0
    while (i < 20 and np.abs(x-xalt) > 1e-7):
        temp = x
        x = phi1(x, xalt)
        xalt = temp
        xrange.append(x)
        i += 1
    return xrange


n = 10

valueRange = np.linspace(0.5, 1, 10)

for n in range(100):
    x = 0.5 + random.random()/2
    xrange = genIteration(x)
    plt.plot(range(len(xrange)), xrange, "-k", label=f"f({x})")


for n in range(100):
    x = 0.5 + random.random()/2
    xalt = 0.5 + random.random()/2
    while (x == xalt):
        xalt = 0.5 + random.random()/2
    xrange = genIterationApprox(x, xalt)
    plt.plot(range(len(xrange)), xrange, "-r", label=f"f({x}) approx")

plt.legend()
plt.show()
