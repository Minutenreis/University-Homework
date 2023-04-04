import matplotlib.pyplot as plt
import numpy as np


def f(x): return 23200658*x**3 - 1083557822*x**2 + 1753426039 * x - 945804881


a = np.double(1.61801916)
b = np.double(1.61801917)

h = np.double(0.0000000001)
xrange = np.arange(a, b+h, h)
plt.plot(xrange, f(xrange), '-x', label='$f(x)$')
plt.legend()
plt.grid(True)
plt.show()
