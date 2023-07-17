import numpy as np
import matplotlib.pyplot as plt


def f(tx):
    return np.cos(np.pi/2 * tx)


def df(tx):
    return -np.pi/2 * np.sin(np.pi/2 * tx)


t = [-2, -1, 0, 1, 2]


# https://en.wikipedia.org/wiki/Tridiagonal_matrix_algorithm
def TDMA(a, b, c, d):
    n = len(d)
    cNew = np.zeros(n-1, float)  # c'[i]
    dNew = np.zeros(n, float)  # d'[i]
    x = np.zeros(n, float)  # x[i]

    cNew[0] = c[0]/b[0]
    dNew[0] = d[0]/b[0]

    for i in range(1, n-1):
        cNew[i] = c[i]/(b[i] - a[i]*cNew[i-1])
    for i in range(1, n):
        dNew[i] = (d[i] - a[i]*dNew[i-1])/(b[i] - a[i]*cNew[i-1])
    x[n-1] = dNew[n-1]
    for i in range(n-2, -1, -1):
        x[i] = dNew[i] - cNew[i]*x[i+1]
    return x


n = len(t)-1  # array starts at 0
h = [t[i+1]-t[i] for i in range(n)]
b = [2 for i in range(n+1)]
lambda1 = [1, *[h[i]/(h[i-1]+h[i]) for i in range(1, n)], 1]  # c
mu = [1, *[h[i-1]/(h[i-1]+h[i]) for i in range(1, n)], 1]  # a
coeff2 = [(f(t[i])-f(t[i-1]))/(t[i]-t[i-1])
          for i in range(1, n+1)]  # f[t_i-1, t_i]
coeff3 = [(coeff2[i]-coeff2[i-1])/(h[i-1]+h[i])
          for i in range(1, len(coeff2))]  # f[t_i-1, t_i, t_i+1]
d = [6*(coeff2[0]-df(t[0]))/h[0],
     *[6*coeff3[i] for i in range(len(coeff3))],
     6*(df(t[n])-coeff2[n-1])/h[n-1]]  # d

M = TDMA(mu, b, lambda1, d)
C = [(f(t[i+1])+f(t[i]))/2 - h[i]**2/12 * (M[i+1]+M[i])
     for i in range(n)]
D = [(f(t[i+1])-f(t[i]))/h[i] - h[i]/6 * (M[i+1]-M[i])
     for i in range(n)]


def spline(tx):
    for i in range(n):
        if t[i] <= tx and tx <= t[i+1]:
            return splineHelp(tx, i)
    print(tx)


def splineHelp(tx, i):
    return C[i] + D[i] * (tx - (t[i]+t[i+1])/2) + M[i+1] * (tx - t[i])**3/(6*h[i]) - M[i] * (tx-t[i+1])**3/(6*h[i])


xRange = np.linspace(t[0], t[-1], 1000)
print("mu =", [round(tx, 3) for tx in mu])
print("lambda1 =", [round(tx, 3) for tx in lambda1])
print("b =", [round(tx, 3) for tx in b])
print("d = ", [round(tx, 3) for tx in d])
print("t =", [round(tx, 3) for tx in t])
print("h =", [round(tx, 3) for tx in h])
print("C =", [round(tx, 3) for tx in C])
print("D =", [round(tx, 3) for tx in D])
print("M =", [round(tx, 3) for tx in M])
print("f =", [round(f(tx), 3) for tx in t])
print("spline =", [round(spline(tx), 3) for tx in t])
plt.plot(xRange, [f(x) for x in xRange], label="f")
plt.plot(xRange, [spline(x) for x in xRange], label="spline")
plt.legend()
plt.show()
