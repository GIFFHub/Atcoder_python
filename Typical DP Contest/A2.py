N = int(input())
M = 100

A = [int(a) for a in input().split()]
X = [[0] * (N * M + 1) for _ in range(N+1)]
X[0][0] = 1

for i, a in enumerate(A):
    for j in range(N*M+1):
        tmp1 = X[i+1][j]
        tmp2 = X[i][j]
        X[i+1][j] = X[i][j]
        if j >= a:
            tmp3 = X[i][j-a]
            X[i+1][j] |= X[i][j-a]
            tmp4 = X[i+1][j]

print(sum(X[N]))