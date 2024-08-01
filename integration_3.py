import numpy as np
import math

q_no = 0


def f(x):
    if q_no == 1:
        return np.sin(x)
    elif q_no == 2:
        return x**2 + x
    elif q_no == 3:
        return x**2
    else:
        return 0


def midpoint(a, b, n):
    result = 0
    del_x = (b - a) / n
    x = a + (del_x / 2)
    for i in range(n):
        result += f(x)
        x += del_x
    return round(del_x * result, 4)


def trapezoidal(a, b, n):
    result = 0
    del_x = (b - a) / n
    x = a
    for i in range(1, n):
        x += del_x
        result += f(x)
        result = result * 2
    result += f(a)
    result += f(b)
    return round(result * (del_x / 2), 4)


def simpsons(a, b, n):
    del_x = (b - a) / n
    x = a
    result = f(x)
    result += f(b)
    for i in range(1, n):
        x += del_x
        if i % 2 == 0:
            result += f(x) * 2
        else:
            f(x) * 4
    return round(result * (del_x / 3), 4)


# 1. sin(x), 0 to pi
q_no = 1
print(midpoint(0, math.pi, 1000))
print(trapezoidal(0, math.pi, 1000))
print(simpsons(0, math.pi, 1000))
print("")

# 2. (x^2 + x), from 0 to 1
q_no = 2
print(midpoint(0, 1, 1000))
print(trapezoidal(0, 1, 1000))
print(simpsons(0, 1, 1000))
print("")

# 3. x^2, from -1 to 1
q_no = 3
print(midpoint(-1, 1, 1000))
print(trapezoidal(-1, 1, 1000))
print(simpsons(-1, 1, 1000))
print("")
