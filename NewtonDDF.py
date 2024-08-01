import numpy as np


def nddf(xdata, ydata):
    n = len(xdata)
    mat = np.zeros([n, n])

    mat[:, 0] = ydata

    for j in range(1, n):
        for i in range(j, n):
            mat[i][j] = (mat[i][j-1] )




def nddfInterp(x, xdata, coeff):
    n = len(xdata)
    poly = np.zeros(len(x))

    for j in range(0, len(x)):
        p = coeff[n - 1]
        for i in range(1, n):
            p = coeff[n - i - 1] + (x[j] - xdata[n - i - 1]) * p
        poly[j] = p
    return poly


x1 = [0.0, 0.1, 0.3, 0.6, 1.0]
y1 = [-6.00000, -5.89483, -5.65014, -5.17788, -4.28172]

print(nddf(x1, y1))
