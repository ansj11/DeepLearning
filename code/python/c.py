import numpy as np

M = input()
N = input()

a = np.empty((M,N))

for i in range(M):
    for j in range(N):
        a[i][j] = input()

m = 0
n = 0
s = 0
for i in range(M+N):
    s += a[m][n]
    tmp = np.random.randint(0,2)
    m += tmp
    n += (1-tmp)

print s