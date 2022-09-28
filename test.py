# -*- coding: utf-8 -*-

# метод хорд
interval = (0, 1)


def f(x):
    return x ** 3 - 12 * x + 6


while interval[-1] - interval[0] > 0.01:

    a, b = f(interval[0]), f(interval[1])
    iter = round(interval[0] - ((interval[1] - interval[0]) * a) / (b - a), 4)
    iter_sign = f(iter)
    # print(iter)
    # print(iter_sign)
    if (a > 0 and iter_sign < 0) or (a < 0 and iter_sign > 0):
        interval = (interval[0], iter)
    if (b > 0 and iter_sign < 0) or (b < 0 and iter_sign > 0):
        interval = (iter, interval[1])



print(interval)

