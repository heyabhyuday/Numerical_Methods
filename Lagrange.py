import numpy as np

# Reading number of unknowns
n = 5

# Making numpy array of n & n x n size and initializing
# to zero for storing x and y value along with differences of y
x = np.zeros(n)
y = np.zeros(n)

x = [0.0, 0.1, 0.3, 0.6, 1.0]
y = [-6.00000, -5.89483, -5.65014, -5.17788, -4.28172]

# Reading interpolation point
xp = 0.25

# Set interpolated value initially to zero
yp = 0

# Implementing Lagrange Interpolation
for i in range(n):

    p = 1

    for j in range(n):
        if i != j:
            p = p * (xp - x[j]) / (x[i] - x[j])

    yp = yp + p * y[i]

# Displaying output
print('Interpolated value at %.3f is %.5f.' % (xp, yp))