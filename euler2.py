import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-poster')
# %matplotlib inline

# Define parameters
f = lambda t, s: np.exp(2*t)  # ODE
h = 0.1  # Step size
t = np.arange(0, 5, h)  # Numerical grid
s0 = 1  # Initial Condition

# Explicit Euler Method
s = np.zeros(len(t))
s[0] = s0

for i in range(0, len(t) - 1):
    s[i + 1] = s[i] + h*f(t[i], s[i])

plt.figure(figsize=(12, 8))
plt.plot(t, s, 'b--', label='Approximate')
plt.plot(t, np.exp(2*t), 'g', label='Exact')
plt.title('Approximate and Exact Solution \
for Simple ODE')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.grid()
plt.legend(loc='lower right')
plt.show()
