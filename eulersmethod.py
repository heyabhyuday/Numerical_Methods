from matplotlib import pyplot as plt
import math


def func(t, y):
    return math.exp(2 * t)


def ImpEuler(f, t0, t, y0, N):
    h = (t - t0) / N
    yt = [y0]
    t = [t0]
    TOL = 0.000001
    max_step = 10000
    h1 = 0.1
    count = 0
    z = 0

    for n in range(0, N + 1):
        t.append(t[n] + h)
        x = yt[n] + h1
        y = yt[n]
        while count <= max_step:
            ffx = x - yt[n] - h * f(t[n + 1], x)
            ffy = y - yt[n] - h * f(t[n + 1], y)
            # print(ffx)
            # print(ffy)
            z = x - ffx * (x - y) / (ffx - ffy)
            if abs((z - x) / z) < TOL:
                yt.append(z)
                break
            y = x
            x = z
            count = count + 1
        return t, yt


solI = ImpEuler(func, 0, 5, 1, 100)
plt.plot(solI[0], solI[1])
plt.show()
