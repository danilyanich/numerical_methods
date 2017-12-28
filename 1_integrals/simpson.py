import math
import matplotlib.pyplot as plt


def f_x(x):
    p = 1.2
    return math.sqrt(p + x ** 2) / (1. + math.cos(p * x))


eps = 10. ** (-5)
max_f_4 = 24.
a = 0
b = 1

if __name__ == '__main__':
    h = (180. * eps / max_f_4) ** (1./4.)
    n = int(1. / h)

    sum_1 = sum(f_x(a + (2*k - 1)*h) for k in range(1, int(n / 2.)))
    sum_2 = sum(f_x(a + (2*k)*h) for k in range(1, int(n / 2.) - 1))

    I = h / 3. * (f_x(a) + f_x(b) + 4. * sum_1 + 2. * sum_2)

    print('simpson')
    print('h: {}'.format(h))
    print('n: {}'.format(n))
    print('I: {}'.format(I))

    x = [a + h*k for k in range(0, n)]
    plt.plot(x, [f_x(x_i) for x_i in x])
    plt.plot([a, b], [I, I])
    plt.show()

