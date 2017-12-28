import math
import matplotlib.pyplot as plt


def dy_dx(x, y):
    return (y + math.sqrt(x ** 2 + y ** 2)) / x


if __name__ == '__main__':
    a, b = 1, 1.5
    n = 10
    h = (b - a) / n

    print('явный метод Эйлера')

    y = [0 for i in range(0, n + 1)]
    for i in range(1, n + 1):
        y[i] = y[i - 1] + h * dy_dx(a + h * i, y[i - 1])

    [print(y_i) for y_i in y]
    plt.plot([a + h * i for i in range(0, n + 1)], y, label='euler')

    print('неявный метод Эйлера')

    y = [0 for i in range(0, n + 1)]
    for i in range(1, n + 1):
        y_km1 = y[i - 1]
        it = 0
        while True:
            f = y_km1 - y[i - 1] - h * dy_dx(a + h * i, y_km1)
            f_dx = 1 - h * dy_dx(a + h * i, y_km1)
            y_k = y_km1 - f / f_dx
            if abs(y_k - y_km1) < 10e-5:
                break
            y_km1 = y_k
            it += 1
        y[i] = y_k

    [print(y_i) for y_i in y]
    plt.plot([a + h * i for i in range(0, n + 1)], y, label='dark euler')

    print('метод средних прямоугольников 2 порядка')

    y = [0 for i in range(0, n + 1)]
    for i in range(1, n + 1):
        x_1, x_2 = a + h * i - h / 2, a + h * (i - 1)
        y[i] = y[i - 1] + h * (dy_dx(x_1, y[i - 1] + h / 2 * dy_dx(x_2, y[i - 1])))

    [print(y_i) for y_i in y]
    plt.plot([a + h * i for i in range(0, n + 1)], y, label='middle triangles')

    print('метод Рунге-Кутта на базе ф-лы Симпсона')

    def fi_0(x, y):
        return h * dy_dx(x, y)

    def fi_1(x, y):
        return h * dy_dx(x + h / 2, y + fi_0(x, y) / 2)

    def fi_2(x_n, x, y):
        return h * dy_dx(x_n, y - fi_0(x, y) + 2 * fi_0(x, y))

    y = [0 for i in range(0, n + 1)]
    for i in range(1, n + 1):
        x_i, x_im1 = a + h * i, a + h * (i - 1)
        y_im1 = y[i - 1]
        y[i] = y_im1 + (fi_0(x_im1, y_im1) + 4 * fi_1(x_im1, y_im1) + fi_2(x_i, x_im1, y_im1)) / 6

    [print(y_i) for y_i in y]
    plt.plot([a + h * i for i in range(0, n + 1)], y, label='runge-kutta')

    print('явный метод Адамса 3 порядка')

    y = [y[i] if i < 3 else 0 for i in range(0, n + 1)]
    for i in range(3, n + 1):
        x_im1, x_im2, x_im3 = (a + h * (i - k) for k in range(1, 4))
        y_im1, y_im2, y_im3 = (y[i - k] for k in range(1, 4))
        y[i] = y_im1 + h * (23 * dy_dx(x_im1, y_im1) - 16 * dy_dx(x_im2, y_im2) + 5 * dy_dx(x_im3, y_im3)) / 12

    [print(y_i) for y_i in y]
    plt.plot([a + h * i for i in range(0, n + 1)], y, label='adams')

    plt.legend()
    plt.show()
