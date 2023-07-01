import numpy as np
import matplotlib.pyplot as plt


def orig(x): return np.sqrt(x)/(1+x)  # f(x)


def subs(x): return 2*x**2/(1+x**2)  # f(x) substituiert


def hGen(n): return [1 / 2**(k+1) for k in range(n+1)]  # h_k


def t(hRange): return [h**2 for h in hRange]  # t(h) = h^2


def T(h, f): return h * (f(0)/2+f(1)/2 +
                         sum([f(i*h) for i in range(1, int(1/h))]))  # summierte Trapezregel


def PFast(h, n, f):  # Nevilles Algorithm iterative, remembering results
    hRange = hGen(n)
    tRange = t(hRange)
    list = [[T(h, f) for h in hRange]]  # list[k][i] = P(i, k)
    for k in range(1, n+1):
        list.append([])
        for i in range(0, k):
            list[k].append(0)
        for i in range(k, n+1):
            list[k].append(list[k-1][i] + (h-tRange[i])/(tRange[i] -
                           tRange[i-k]) * (list[k-1][i] - list[k-1][i-1]))
    return list[n][n]


nRange = [1, 2, 4, 8]
resultRangeOrig = [PFast(0, n, orig) for n in nRange]
resultRangeSubs = [PFast(0, n, subs) for n in nRange]
integralExact = 2 - np.pi/2

for n in range(4):
    integralApproxOrig = resultRangeOrig[n]
    integralApproxSubs = resultRangeSubs[n]
    print()
    print("n =", nRange[n])
    print("Integral approx. orig =", integralApproxOrig)
    print("absoluter Fehler      =", abs(integralApproxOrig - integralExact))
    print("Integral approx. subs =", integralApproxSubs)
    print("absoluter Fehler      =", abs(integralApproxSubs - integralExact))

plt.plot(nRange, [np.abs(i-integralExact) for i in resultRangeOrig], "-",
         label="absoluter Fehler Romberg orig")
plt.plot(nRange, [np.abs(i-integralExact) for i in resultRangeSubs], "-",
         label="absoluter Fehler Romberg subs")
plt.yscale("log")
plt.legend()
plt.show()
