import math
import numpy as np
import matplotlib.pyplot as plt


def K_x_s(x, s):
    return math.sin(x + s)


def f_x(x):
    return 1 + math.sin(x)


def A_k(k):
    return 0 if k == 0 else h


if __name__ == '__main__':
    a, b = 0, math.pi / 2
    steps = 10
    h = (b - a) / steps
    L = 0.1

    print('и.у. Вольтерра 2 рода')
    print('метод механических квадратур')

    f = np.array([f_x(a + h * k) for k in range(0, steps + 1)])
    A = np.array([[A_k(j) * K_x_s(a + h * i, a + h * j) if i >= j else 0 for j in range(0, steps + 1)] for i in range(0, steps + 1)])
    A = np.subtract(np.identity(steps + 1), A)

    y = np.linalg.solve(A, f)

    [print(y_i) for y_i in y]
    plt.plot([a + h * i for i in range(0, steps + 1)], y)

    print('метод последовательных приближений')

    eps = 10e-5
    y_k = [f_x(a + h * i) for i in range(0, steps + 1)]
    y_km1 = [0 for i in range(0, steps + 1)]
    y = [0 for i in range(0, steps + 1)]

    while True:
        y_km1 = np.copy(y_k)
        for i in range(0, steps + 1):
            x_i = a + h*i
            I = h * sum([K_x_s(x_i, a + h*k) * y_km1[k] for k in range(0, i + 1)])
            y_k[i] = L * I + f_x(x_i)
            y[i] += y_k[i]
        if np.linalg.norm(np.subtract(y_k, y_km1)) < eps:
            break

    [print(y_i) for y_i in y]
    plt.plot([a + h * i for i in range(0, steps + 1)], y)

    plt.show()


