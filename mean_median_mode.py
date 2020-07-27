import statistics as st
import numpy as np
N = int(input())
A = list(map(int, input().split()[:N]))
print(round(st.mean(A), 1))
print(round(st.median(A), 1))
A.sort()
U = np.unique(A)
U.sort()
UL = len(U)
Max = 1
for i in range(UL):
    x = A.count(U[i])
    if x>Max :
        Max = x
        mode = U[i]
if (Max == 1):
    mode = A[0]
print(mode)
