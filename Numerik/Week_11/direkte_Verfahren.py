import numpy as np
# input
A = np.array([[0.1341, -0.2665], [-0.2665, 1.623]])
b = np.array([-0.9322, -0.9352])
P = np.array([[0, 1], [1, 0]])
L = np.array([[1, 0], [-0.5032, 1]])
R = np.array([[-0.2665, 1.623], [0, 0.5502]])
digits = 4  # rounding
nachiterationen = 1


Pb = P @ b


def cRound(x):
    return float(np.format_float_positional(x, precision=digits, unique=False, fractional=False, trim='k'))


def round2DArr(x):
    for i in range(len(x)):
        for j in range(len(x[0])):
            x[i][j] = cRound(x[i][j])
    return x


def round2DArrL(x):
    for i in range(len(x)):
        for j in range(len(x[0])):
            x[i][j] = cRoundL(x[i][j])
    return x


def roundArr(x):
    for i in range(len(x)):
        x[i] = cRound(x[i])
    return x


def roundArrL(x):
    for i in range(len(x)):
        x[i] = cRoundL(x[i])
    return x


def cRoundL(x):
    return float(np.format_float_positional(x, precision=digits*2, unique=False, fractional=False, trim='k'))


# Löse Ly = Pb
def Lyb(L, Pb):
    y = np.zeros(2)
    y[0] = cRoundL(Pb[0])
    y[1] = cRoundL(Pb[1] - cRoundL(L[1, 0] * y[0]))
    return y


y = Lyb(L, Pb)

# Löse Rx = y


def RxY(R, y):
    x = np.zeros(2)
    x[1] = cRound(y[1] / R[1, 1])
    x[0] = cRound(cRound(y[0] - cRound(R[0, 1] * x[1]))/R[0, 0])
    return x


x = RxY(R, y)

print("x = ", x)

for i in range(nachiterationen):
    delta = roundArr(b - roundArrL(A @ x))
    y = Lyb(L, delta)
    h = RxY(R, y)
    x = roundArr(x + h)
    print("x = ", x)
