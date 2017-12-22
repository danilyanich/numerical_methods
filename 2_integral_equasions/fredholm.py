import math
import numpy as np


def K_x_s(x, s):
    return math.sin(x + s)


def f_x(x):
    return 1 + math.sin(x)


def A_k(k):
    return  h


if __name__ == '__main__':
    a, b = 0, math.pi / 2
    steps = 10
    h = (b - a) / steps

    print('и.у. фредгольма 2 рода')
    print('метод механических квадратур')

    f = np.array([f_x(a + h * k) for k in range(0, steps + 1)])
    A = np.array([[A_k(i) * K_x_s(a + h * i, a + h * j) for i in range(0, steps + 1)] for j in range(0, steps + 1)])
    A = np.subtract(np.identity(steps + 1), A)

    y = np.linalg.solve(A, f)
    [print(y_i) for y_i in y]
