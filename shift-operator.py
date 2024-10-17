# It's not hard to show that (exp(d/dt)f)(t) = f(t + 1)
# We can verify with a matrix

import numpy as np
import scipy.linalg
import matplotlib.pyplot as plt

N = 100
a = 10

M = np.zeros((N, N))
for i in range(N):
    M[i, i - 1] = -a / 2
    M[i, (i + 1) % N] = a / 2

data = np.sin(np.linspace(0, 2 * np.pi, N))

plt.plot(data, label="$f(t)$")
plt.plot(scipy.linalg.expm(M) @ data, label="$f(t + a)$")
plt.legend()
plt.show()
