import matplotlib.pyplot as plt
import numpy as np


def f(x): return np.log(3/2+x)
def g(x): return np.log(3/2) + 2/3*x - 2/9 * x**2
def h(x): return 0.6373/2 + 0.4941*3/2*x - 0.0497 * 45/8 * (x**2-1/3)


xrange = np.arange(-1, 1.05, 0.05)
plt.plot(xrange, f(xrange), 'b-', label='$f(x) = ln(3/2+x)$')
plt.plot(xrange, g(xrange), 'g-', label='$F(x) = T_2f(x,0)$')
plt.plot(xrange, h(xrange), 'r-', label='$f*(x)$ = Lotfußpunkt')
plt.plot(xrange, np.abs(f(xrange)-g(xrange)), 'c-', label='|f(x)-F(x)|')
plt.plot(xrange, np.abs(f(xrange)-h(xrange)), 'y-', label='|f(x)-f*(x)|')
plt.xlabel('x')
plt.ylabel('y')
plt.title("Vergleich Approximationen")
plt.legend()
plt.grid(True)
plt.show()
