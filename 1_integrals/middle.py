import math


def f_x(x):
    p = 1.2
    return math.sqrt(p + x ** 2) / (1. + math.cos(p * x))


eps = 10. ** (-5)
max_f_2 = 3.
a = 0
b = 1

if __name__ == '__main__':
    h = math.sqrt(24.*eps/max_f_2)
    n = int(1. / h)
    I = h * sum(f_x(a + k*h) for k in range(0, n - 1))

    print('middle')
    print('h: {}'.format(h))
    print('n: {}'.format(n))
    print('I: {}'.format(I))

