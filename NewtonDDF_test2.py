import numpy as np


def nddf(x, y):
    n = len(x)
    coeff = []
    for i in range(n):
        coeff.append(y[i])
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            coeff[i] = float(coeff[i] - coeff[i-1])/float(x[i] - x[i-j])
    return np.array(coeff)


def interpolate(coeff, xset, x):
    n = len(coeff) - 1
    result = coeff[n] + (x - xset[n])
    for i in range(n-1, -1, -1):
        result = result * (x - xset[i]) + coeff[i]
    return result


xdata = [0.0, 0.1, 0.3, 0.6, 1.0]
ydata = [-6.00000, -5.89483, -5.65014, -5.17788, -4.28172]
val = 0.25
coefs = nddf(xdata, ydata)
interpolation_result = round(interpolate(coefs, xdata, val), 5)
print(f"At x = {val}, NDDF says the value will be {interpolation_result}")
