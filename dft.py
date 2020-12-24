import numpy as np

def dft(x):
    x = np.asarray(x, dtype=int)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)


# Driver program 

x = np.random.random(1024)
dft(x)