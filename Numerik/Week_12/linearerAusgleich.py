import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return -21/10 * x + 39/34 * x**2


def g(x):
    return x**2


xRange = np.linspace(-2, 2, 1000)
plt.plot(xRange, f(xRange), label="f(x)")
plt.plot([-2, -1, 1, 2], [9, 3, 0, 0], "x", label="b")
plt.legend()
plt.show()
