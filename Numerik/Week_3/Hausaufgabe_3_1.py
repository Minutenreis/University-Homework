import numpy as np
import matplotlib.pyplot as plt


def x_k(n, i): return -5 + 10*i/n if n > 0 else 0


def f(x): return 1/(1+x**2)


# def y_k(n, i): return 1/(1+x_k(n, i)**2)


def genInterpolation(n): return lambda x: np.sum(
    [f(x_k(n, i)) *
     np.prod([(x-x_k(n, j))/(x_k(n, i)-x_k(n, j))
             for j in range(n+1) if j != i])
     for i in range(n+1)])


xrange = np.linspace(-5, 5, 10000)

nRange = list(range(6))
nRange.append(10)

for n in nRange:
    P = genInterpolation(n)
    plt.plot(xrange, list(map(P, xrange)), label=f"$P(x,{n})$")

plt.plot(xrange, f(xrange), "-k", label='$f(x)$')
plt.legend()
plt.grid(True)
plt.show()
