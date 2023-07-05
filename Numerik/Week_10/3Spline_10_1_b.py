import numpy as np
import matplotlib.pyplot as plt


def f(tx):
    return np.cos(np.pi * tx/2)


M = [0, 6/7, -24/7, 6/7, 0]
t = [-2, -1, 0, 1, 2]
h = [t[i+1]-t[i] for i in range(len(t)-1)]
C = [(f(t[i+1])+f(t[i]))/2 - h[i]**2/12 * (M[i+1]+M[i])
     for i in range(len(t)-1)]
D = [(f(t[i+1])-f(t[i]))/h[i] - h[i]/6 * (M[i+1]-M[i])
     for i in range(len(t)-1)]


def spline(tx):
    for i in range(len(t)-1):
        if t[i] <= tx and tx <= t[i+1]:
            return splineHelp(tx, i)
    print(tx)


def splineHelp(tx, i):
    return C[i] + D[i] * (tx - (t[i]+t[i+1])/2) + M[i+1] * (tx - t[i])**3/(6*h[i]) - M[i] * (tx-t[i+1])**3/(6*h[i])


xRange = np.linspace(-2, 2, 1000)
print("t =", t)
print("h =", h)
print("C =", C)
print("D =", D)
print("M =", M)
print("f =", [f(tx) for tx in t])
print("spline =", [round(spline(tx), 3) for tx in t])
plt.plot(xRange, f(xRange), label="f")
plt.plot(xRange, [spline(x) for x in xRange], label="spline")
plt.legend()
plt.show()
