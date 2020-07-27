import statistics as np
N = int(input())
A = list(map(int, input().split()[:N]))
F = list(map(int, input().split()[:N]))
Arr = []
for i in range(N):
    for j in range(F[i]):
        Arr.append(A[i])
Arr.sort()
N = len(Arr)
if N % 2 == 0 :
    A1 = Arr[:int((N/2))]
    A2 = Arr[int((N/2)):N]
else :
    m = (N//2)
    A1 = Arr[:m]
    A2 = Arr[(m+1):N]
Q1 = np.median(A1)
Q3 = np.median(A2)
print(round(float(Q3-Q1), 1))