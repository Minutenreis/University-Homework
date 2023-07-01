import numpy as np
import matplotlib.pyplot as plt


def orig(x): return np.sqrt(x)/(1+x)  # f(x)


def subs(x): return 2*x**2/(1+x**2)  # f(x) substituiert


def hGen(nRange): return [1 / k for k in nRange]  # h_k


def t(hRange): return [h**2 for h in hRange]  # t(h) = h^2


def T(h, f): return h * (f(0)/2+f(1)/2 +
                         sum([f(i*h) for i in range(1, int(1/h))]))  # summierte Trapezregel


def PFast(h, n, f, nRange):  # Nevilles Algorithm iterative, remembering results
    hRange = hGen(nRange)
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
resultOrig = PFast(0, 3, orig, nRange)
resultSubs = PFast(0, 3, subs, nRange)
integralExact = 2 - np.pi/2

integralApproxOrig = resultOrig
integralApproxSubs = resultSubs
print()
print("Integral approx. orig =", integralApproxOrig)
print("absoluter Fehler orig =", abs(integralApproxOrig - integralExact))
print("Integral approx. subs =", integralApproxSubs)
print("absoluter Fehler subs =", abs(integralApproxSubs - integralExact))
