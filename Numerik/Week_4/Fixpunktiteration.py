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
    while (i < 20 and abs(x-xalt) > 1e-7):
        xalt = x
        x = phi(x)
        xrange.append(x)
        i += 1
    return xrange


def genIteration1(x, xalt,):
    xrange = [x]
    i = 0
    while (i < 20 and abs(x-xalt) > 1e-7):
        temp = x
        x = phi1(x, xalt)
        xalt = temp
        xrange.append(x)
        i += 1
    return xrange


n = 10

valueRange = np.linspace(0.5, 1, 10)

# x = 0.999999999999412
# y = 0.6568433
# z = 0.6568433

# xrange = genIteration(x)
# yrange = genIteration(y)
# zrange = genIteration(z)

# plt.plot(range(len(xrange)), xrange, label=f"f({x})")
# plt.plot(range(len(yrange)), yrange, label=f"f({y})")
# plt.plot(range(len(zrange)), zrange, label=f"f({z})")

# for x in valueRange:
#     xrange = genIteration(x)
#     plt.plot(range(len(xrange)), xrange, label=f"f({x})")

for n in range(10):
    x = 0.5 + random.random()/2
    xrange = genIteration(x)
    plt.plot(range(len(xrange)), xrange, label=f"f({x})")

# x = 0.999999999999412
# y = 0.6568433
# z = 0.823423
# xalt = 0.6
# yalt = 0.6
# zalt = 0.8

# xrange = genIteration1(x, xalt)
# yrange = genIteration1(y, yalt)
# zrange = genIteration1(z, zalt)

# plt.plot(range(len(xrange)), xrange, label=f"f({x}) approx")
# plt.plot(range(len(yrange)), yrange, label=f"f({y}) approx")
# plt.plot(range(len(zrange)), zrange, label=f"f({z}) approx")

plt.legend()
plt.show()
