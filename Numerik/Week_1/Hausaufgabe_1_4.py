import numpy as np
import matplotlib.pyplot as plt


def f(x): return 223200658*(x**3) - 1083557822 * \
    (x**2) + 1753426039 * x - 945804881


a = np.double(1.61801916)
b = np.double(1.61801917)

h = np.double(0.00000000002)
xrange = np.linspace(a, b, 100)
plt.plot(xrange, f(xrange), label='$f(x)$')
plt.legend()
plt.grid(True)
plt.show()
