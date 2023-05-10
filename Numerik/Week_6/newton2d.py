import numpy as np
import matplotlib.pyplot as plt

# F(x,y,z)


def F(x, y, z): return np.array([[x**2+10*y*z], [20*y**2*z + 3*x*z - 5]])

# Inverse of Jacobimatrix of f(y,z)=F(x,y,z) (x is constant)


def Jfinv(x, y, z): return 1/(20*y**2*z+30*x*y) * \
    np.array([[-2*y**2, y], [4*y*z+3/10*x, -z]])

# Newton-Funktion


def Nf(x, y, z): return np.array(
    [[y], [z]]) - np.dot(Jfinv(x, y, z), F(x, y, z))

# Newton-Verfahren


def Newton(x, y, z, maxit):
    for i in range(maxit):
        [y], [z] = Nf(x, y, z)
        if np.abs(F(x, y, z)[0][0]) < 10**(-8) and np.abs(F(x, y, z)[1][0]) < 10**(-8):
            return y, z
    print(x)  # find if maxit is sufficient
    return y, z


xrange = np.linspace(-3, -0.5, 1000)

for x in xrange:
    y, z = Newton(x, 1, 1, 1000)
    plt.scatter(y, z, s=9, c="r", marker=".")

plt.ylabel("z")
plt.xlabel("y")
plt.show()
