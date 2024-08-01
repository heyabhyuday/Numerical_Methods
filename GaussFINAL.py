import numpy as np


def GE(coeff, const):
    n = len(const)

    for i in range(n):
        max_index = i
        for j in range(i + 1, n):
            if abs(coeff[j][i]) > abs(coeff[max_index][i]):
                max_index = j
        coeff[i], coeff[max_index] = coeff[max_index], coeff[i]
        const[i], const[max_index] = const[max_index], const[i]
        for k in range(i + 1, n):
            factor = coeff[k][i] / coeff[i][i]
            for l in range(i, n):
                coeff[k][l] -= factor * coeff[i][l]
            const[k] -= factor * const[i]

    res = np.zeros(n)
    for i in range(n - 1, -1, -1):
        res[i] = const[i] / coeff[i][i]
        for j in range(i - 1, -1, -1):
            const[j] -= coeff[j][i] * res[i]
    return res


def GJE(coeff, const):
    n = len(const)

    for i in range(n):
        pvt = coeff[i][i]
        for j in range(i + 1, n):
            factor = coeff[j][i] / pvt
            for k in range(n):
                coeff[j][k] -= factor * coeff[i][k]
            const[j] -= factor * const[i]

    for i in range(n - 1, -1, -1):
        pvt = coeff[i][i]
        for j in range(i - 1, -1, -1):
            factor = coeff[j][i] / pvt
            for k in range(n):
                coeff[j][k] -= factor * coeff[i][k]
            const[j] -= factor * const[i]

    res = np.zeros(n)
    for i in range(n):
        res[i] = const[i] / coeff[i][i]
    return res


A = np.array([[1, 1, 1], [4, 3, -1], [3, 5, 3]], dtype=float)
B = np.array([1, 6, 4], dtype=float)

ans1 = GE(A, B)
print("Gaussian Elimination yields", ans1)
ans2 = GJE(A, B)
print("Gauss-Jordan Elimination yields", ans2)
