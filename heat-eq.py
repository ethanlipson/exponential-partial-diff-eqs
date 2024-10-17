import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg

N = 100
c = 0.1
T = 1000

laplacian = np.zeros((N, N))
for i in range(N):
    laplacian[i, i - 1] = 1
    laplacian[i, i] = -2
    laplacian[i, (i + 1) % N] = 1

u = np.random.rand(N)
lo = np.min(u)
hi = np.max(u)

for t in range(T):
    current = scipy.linalg.expm(c * t * laplacian) @ u
    plt.clf()
    plt.ylim(lo, hi)
    plt.plot(current)
    plt.pause(0.01)
