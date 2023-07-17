import numpy as np
import matplotlib.pyplot as plt
import time


def f(x): return x * np.sin(x)  # f(x)


def hGen(n): return [1 / 2**(k+1) for k in range(n+1)]  # h_k


def t(hRange): return [h**2 for h in hRange]  # t(h) = h^2


def S(h): return (f(0.5+h) - f(0.5-h)) / (2*h)  # f'(x) approx


def df(x): return np.sin(x) + x * np.cos(x)  # f'(x)


def PHelp(i, k, hRange, h):  # Nevilles Algorithm
    if k == 0:
        return S(hRange[i])
    else:
        # P(i, k-1), to not calculate it twice
        P_i_kMinus1 = PHelp(i, k-1, hRange, h)
        return P_i_kMinus1 + (h-hRange[i])/(hRange[i]-hRange[i-k]) * (P_i_kMinus1 - PHelp(i-1, k-1, hRange, h))


def P(h, n):  # Nevilles Algorithm
    return PHelp(n, n, t(hGen(n)), h)


def PFast(h, n):  # Nevilles Algorithm iterative, remembering results
    tRange = t(hGen(n))
    list = [[S(t) for t in tRange]]  # list[k][i] = P(i, k)
    for k in range(1, n+1):
        list.append([])
        for i in range(0, k):
            list[k].append(0)
        for i in range(k, n+1):
            list[k].append(list[k-1][i] + (h-tRange[i])/(tRange[i] -
                           tRange[i-k]) * (list[k-1][i] - list[k-1][i-1]))
    return list[n][n]


resultRange = [P(0, n) for n in range(1, 9)]
resultRangeFast = [PFast(0, n) for n in range(1, 9)]
dfExact = df(0.5)

print("\nf'(0.5) =", df(0.5))
for n in range(1, 9):
    dfApprox = resultRange[n-1]
    print()
    print("n =", n)
    print("f'Approx(0.5)    =", dfApprox)
    print("absoluter Fehler =", abs(dfApprox - dfExact))
    print("relativer Fehler =", abs(dfApprox - dfExact) / abs(dfExact))

plt.plot(range(1, 9), np.abs(resultRange-dfExact), "-",
         label="absoluter Fehler Neville")
plt.plot(range(1, 9), np.abs(resultRangeFast-dfExact), ".",
         label="absoluter Fehler Neville Fast")
plt.yscale("log")
plt.legend()
plt.show()
