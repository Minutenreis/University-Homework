import numpy as np
import matplotlib.pyplot as plt

x0 = np.double(0.5)


def f(x): return x * np.sin(x)


def df(x): return np.sin(x) + x * np.cos(x)


dfx = df(x0)


def D(h): return (f(x0 + h) - f(x0))/h


def S(h): return (f(x0 + h) - f(x0 - h))/(np.multiply(2, h))


def absD(h): return np.abs(D(h) - dfx)


def absS(h): return np.abs(S(h) - dfx)


h = np.double(0.25)

print('df(x0) =', df(x0))
print()


for i in range(20):
    print("h = 0.25^", i+1)  # h begins with 0.25^1 at i = 0
    print("|D(h) = -f'(x0)|", f"{np.abs(dfx - D(h)):.10E}")
    print("|S(h) = -f'(x0)|", f"{np.abs(dfx - S(h)):.10E}")
    print()
    h = h * np.double(0.25)

start = 14
end = 20
hrange = [0.25**i for i in range(start, end+1)]
plt.plot(range(start, end+1), absD(hrange), label="|D(h)-f'(x0)|")
plt.plot(range(start, end+1), absS(hrange), label="|S(h)-f'(x0)|")
plt.xlabel("n; h = 0.25^n")
plt.ylabel("Error")
plt.legend()
plt.grid(True)
plt.show()
