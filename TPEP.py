xdata = [0.0, 0.1, 0.3, 0.6, 1.0]
ydata = [-6.00000, -5.89483, -5.65014, -5.17788, -4.28172]


def l_interpolation(x):
    result = 0
    for i in range(len(xdata)):
        p = 1
        for j in range(len(xdata)):
            if i != j:
                p = p * (x - xdata[j]) / (xdata[i] - xdata[j])
        result = result + p * ydata[i]
    return round(result, 5)


def three_point(x_val, h):
    x_val, h = float(x_val), float(h)
    a = l_interpolation(x_val)
    b = l_interpolation(x_val + h)
    c = l_interpolation(x_val + 2 * h)
    x_der = ((-3 * a) + (4 * b) - c) / (2 * h)
    return x_der


for x in xdata:
    print(round(three_point(x, 0.1), 5), " ", round(three_point(x, 0.01), 5))
