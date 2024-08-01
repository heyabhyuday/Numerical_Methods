def l_interpolation(xset, yset, x):
    result = 0
    for i in range(len(xset)):
        p = 1
        for j in range(len(xset)):
            if i != j:
                p = p * (x - xset[j]) / (xset[i] - xset[j])
        result = result + p * yset[i]
    return round(result, 5)


xdata = [0.0, 0.1, 0.3, 0.6, 1.0]
ydata = [-6.00000, -5.89483, -5.65014, -5.17788, -4.28172]
x_val = 0.3
interpolation_result = l_interpolation(xdata, ydata, x_val)
print(f"At x = {x_val}, Lagrange says the value will be {interpolation_result}")
