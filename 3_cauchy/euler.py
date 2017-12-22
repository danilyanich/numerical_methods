import math


def dy_dx(x, y):
    return (y + math.sqrt(x ** 2 + y ** 2)) / x


if __name__ == '__main__':
    a, b = 1, 1.5
    n = 10
    h = (b - a) / n

    print('явный метод эйлера')

    y = [0 for i in range(0, n + 1)]
    for i in range(1, n + 1):
        y[i] = y[i-1] + h * dy_dx(a + h * i, y[i-1])

    [print(y_i) for y_i in y]

    print('неявный метод эйлера')

    y = [0 for i in range(0, n + 1)]
    for i in range(1, n + 1):
        y_km1 = y[i - 1]
        it = 0
        while True:
            f = y_km1 - y[i - 1] - h * dy_dx(a + h*i, y_km1)
            f_dx = 1 - h * dy_dx(a + h*i, y_km1)
            y_k = y_km1 - f / f_dx
            if abs(y_k - y_km1) < 10e-5:
                break
            y_km1 = y_k
            it += 1
        y[i] = y_k

    [print(y_i) for y_i in y]
