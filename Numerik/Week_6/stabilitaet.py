import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return (np.sqrt(1+x**2)-1)/x**2


def g(x):
    return 1/(np.sqrt(1+x**2)+1)


start = np.double(1e-6)
end = np.double(1e-5)

x = np.linspace(start, end, 1000)

plt.plot(x, f(x), label="f(x)")
plt.plot(x, g(x), label="g(x)")
plt.legend()
plt.show()
