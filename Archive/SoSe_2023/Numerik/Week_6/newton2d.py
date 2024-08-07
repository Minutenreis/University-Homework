import numpy as np
import matplotlib.pyplot as plt

# F(x,y,z)


def F(x, y, z): return np.array([[x**2+10*y*z], [20*y**2*z + 3*x*y - 5]])

# Inverse of Jacobimatrix of f(y,z)=F(x,y,z) (x is constant)


def Jfinv(x, y, z): return 1/(20*y**2*z+3*x*y) * \
    np.array([[-2*y**2, y], [4*y*z+3/10*x, -z]])

# Newton-Funktion


def Nf(x, y, z): return np.array([[y], [z]]) - Jfinv(x, y, z) @ F(x, y, z)


def Nf2(x, y, z): return np.array([[y], [z]])-1/(20*y**2*z+3*x*y) * np.array(
    [[-2*y**2*x**2+3*x*y**2-5*y], [4*x**2*y*z+20*y**2*z**2+3/10*x**3+5*z]])


# Newton-Verfahren


def Newton(x, y, z, maxit):
    for i in range(maxit):
        [y], [z] = Nf(x, y, z)
        [F1], [F2] = F(x, y, z)
        if np.abs(F1) < 10**(-8) and np.abs(F2) < 10**(-8):
            return y, z
    print(x)  # find if maxit is sufficient
    return y, z


xrange = np.linspace(-3, -0.5, 1000)

yValues = []
zValues = []

for x in xrange:
    y, z = Newton(x, 0.2, 1, 1000)
    yValues.append(y)
    zValues.append(z)

plt.plot(yValues, zValues)
plt.ylabel("z")
plt.xlabel("y")
plt.show()
