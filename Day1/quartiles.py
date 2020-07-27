import statistics as np
N = int(input())
A = list(map(int, input().split()[:N]))
A.sort()
Q2 = np.median(A)
if N % 2 == 0 :
    A1 = A[:int((N/2))]
    A2 = A[int((N/2)):N]
    Q1 = np.median(A1)
    Q3 = np.median(A2)
else :
    m = (N//2)
    A1 = A[:m]
    A2 = A[(m+1):N]
    Q1 = np.median(A1)
    Q3 = np.median(A2)
print(int(Q1))
print(int(Q2))
print(int(Q3))