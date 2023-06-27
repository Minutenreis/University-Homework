import numpy as np
import matplotlib as mat

formatter = mat.ticker.EngFormatter()


d = 700 * 10**(-9)
n = 1.35


def f(k):
    return d * n * 4 / (2 * k)


for k in range(1, 6):
    print(k, formatter(f(k))+"m")
