N = int(input())
A = list(map(int, input().split()[:N]))
W = list(map(int, input().split()[:N]))
x = 0, y = 0
for i in range(N):
  x += A[i] * W[i]
  y += W[i]
print(round((x/y), 1))