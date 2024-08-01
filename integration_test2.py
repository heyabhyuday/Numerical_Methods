import numpy as np
import math




def midpoint(a, b, n):
    result = 0
    del_x = (b - a) / n
    x = a + (del_x / 2)
    for i in range(n):
        result += np.sin(x)
        x += del_x
    return del_x * result



def trapezoidal(a, b, n):
    result = 0
    del_x = (b - a) / n
    x = a
    for i in range(1, n):
        x += del_x
        result += np.sin(x)
        result = result * 2
    result += np.sin(a)
    result += np.sin(b)
    return result * (del_x / 2)


def simpsons(a, b, n):
    del_x = (b - a) / n
    x = a
    result = np.sin(x)
    result += np.sin(b)
    for i in range(1, n):
        x += del_x
        if i % 2 == 0:
            result += np.sin(x) * 2
        else:
            np.sin(x) * 4
    return result * (del_x / 3)





# 1. sin(x), 0 to pi
midpoint(0, math.pi, 1000)
trapezoidal(0, math.pi, 1000)
simpsons(0, math.pi, 1000)

# 2. (x^2 + x), from 0 to 1
midpoint(0, 1, 1000)


# 3. x^2, from -1 to 1
midpoint(-1, 1, 1000)

