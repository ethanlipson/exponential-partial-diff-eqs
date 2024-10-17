import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg

N = 150
c = 0.1
T = 1000

# M has the form
# [[0,         I],
#  [c * Delta, 0]]
# where I is the identity and Delta is the Laplacian
M = np.zeros((N * 2, N * 2))
for i in range(N):
    M[i + N, (i - 1) % N] = c
    M[i + N, i] = -2 * c
    M[i + N, (i + 1) % N] = c
    M[i, i + N] = 1

# w has the form [u, du/dt]
u = np.exp(-((np.linspace(-1, 1, N) * N / 20) ** 2))
w = np.concat((u, np.zeros(N)))
max_mag = np.max(np.abs(w))

for t in range(T):
    current = scipy.linalg.expm(t * M) @ w
    plt.clf()
    plt.ylim(-2 * max_mag, 2 * max_mag)
    plt.plot(current[:N])
    plt.pause(0.01)
