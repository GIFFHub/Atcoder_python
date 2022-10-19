N, X = map(int, input().split())

A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)


# dp[i][j] : i回目のジャンプ後に座標jにいられるかどうか
dp = [[False]*(X+1) for _ in range(N+1)]

dp[0][0] = True

for i in range(1, N+1):
    for j in range(1, X+1):
        if j-A[i-1] >= 0 and j-B[i-1] >= 0:
            dp[i][j] = dp[i-1][j-A[i-1]] or dp[i-1][j-B[i-1]]
        elif j - A[i-1] >= 0:
            dp[i][j] = dp[i-1][j-A[i-1]]
        elif j - B[i-1] >= 0:
            dp[i][j] = dp[i-1][j-B[i-1]]


if dp[N][X]:
    print('Yes')
else:
    print('No')
