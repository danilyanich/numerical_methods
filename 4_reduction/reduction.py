import math
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return 1 / (math.cos(x) ** 2)


def p(x):
    return 1


def q(x):
    return -2 / (math.cos(x) ** 2)


if __name__ == '__main__':
    al_0, be_0, ga_0 = 1, 0, 0
    al_1, be_1, ga_1 = 0, 1, math.cos(0.5) ** 2
    a, b = 0, 0.5

    n = 10
    h = (b - a) / n

    y = [0 for i in range(0, n + 1)]
    x = [a + h * k for k in range(0, n + 1)]


    def solve_1():
        y1 = np.zeros(n + 1)
        y2 = np.zeros(n + 1)
        for i in range(0, n):
            y1[i + 1] = y1[i] + h * (y2[i] + h / 2.0 * (f(x[i]) - p(x[i]) * y2[i] - q(x[i]) * y1[i]))
            y2[i + 1] = y2[i] + h * (f(x[i] + h / 2.0) - p(x[i] + h / 2.0) * (y2[i] + h / 2.0 * (f(x[i]) - p(x[i]) * y2[i] - q(x[i]) * y1[i])) - q(x[i] + h / 2.0) * (y1[i] + h / 2.0 * y2[i]))
        return y1, y1[len(y1) - 1], y2[len(y2) - 1]


    def solve_2():
        y1 = np.zeros(11)
        y2 = np.zeros(11)
        y1[0] = 1
        for i in range(0, 10):
            y1[i + 1] = y1[i] + h * (y2[i] + h / 2.0 * (-p(x[i]) * y2[i] - q(x[i]) * y1[i]))
            y2[i + 1] = y2[i] + h * (-p(x[i] + h / 2.0) * (y2[i] + h / 2.0 * (-p(x[i]) * y2[i] - q(x[i]) * y1[i])) - q(x[i] + h / 2.0) * (y1[i] + h / 2.0 * y2[i]))
        return y1, y1[len(y1) - 1], y2[len(y2) - 1]


    def solve_3():
        y1 = np.zeros(11)
        y2 = np.zeros(11)
        y2[0] = 1
        for i in range(0, 10):
            y1[i + 1] = y1[i] + h * (y2[i] + h / 2.0 * (-p(x[i]) * y2[i] - q(x[i]) * y1[i]))
            y2[i + 1] = y2[i] + h * (-p(x[i] + h / 2.0) * (y2[i] + h / 2.0 * (-p(x[i]) * y2[i] - q(x[i]) * y1[i])) - q(x[i] + h / 2.0) * (y1[i] + h / 2.0 * y2[i]))
        return y1, y1[len(y1) - 1], y2[len(y2) - 1]


    def constants(y_11, y_12, y_21, y_22,  y_31, y_32):
        C1 = (ga_0 - be_0) / al_0
        C2 = ((ga_1 - al_1 * (y_11 + C1 * y_22) - be_1 * (y_12 + C1 * y_22)) / (al_1 * y_31 + be_1 * y_32))
        return C1, C2

    y_first, y_11, y_12 = solve_1()
    y_second, y_21, y_22 = solve_2()
    y_third, y_31, y_32 = solve_3()

    C1, C2 = constants(y_11, y_12, y_21, y_22, y_31, y_32)

    print('C1={} C2={}'.format(C1, C2))

    y = [y_first[i] + C1 * y_second[i] + C2 * y_third[i] for i in range(0, n + 1)]

    [print(y_i) for y_i in y]
    plt.plot([a + h * i for i in range(0, n + 1)], y)

    plt.show()
