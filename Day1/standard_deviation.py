import statistics as st
import math
N = int(input())
A = list(map(int, input().split()[:N]))
s = 0
M = st.mean(A)
for i in range(N):
    s += (A[i]-M)**2
SD = math.sqrt(s/N)
print(round(SD, 1))