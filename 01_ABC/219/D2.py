

if __name__ == '__main__':
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    # dp[i][j][k] : i個目までの弁当使って、たこ焼きj個、たい焼きk個にするのに必要な最小個数

    dp = [[[301 for _ in range(Y+1)] for _ in range(X+1)] for _ in range(N+1)]

    for i in range(N+1):
        for j in range(X+1):
            for k in range(Y+1):
                if j == 0 and k == 0:
                    dp[i][j][k] = 0

    for i in range(1, N+1):
        for j in range(X+1):
            for k in range(Y+1):
                dp[i][min(j+A[i-1], X)][min(k+B[i-1], Y)] = min(dp[i][min(j+A[i-1], X)][min(k+B[i-1], Y)], dp[i-1][j][k] + 1)
                dp[i][j][k] = min(dp[i][j][k], dp[i-1][j][k])

    ans = dp[N][X][Y]
    if ans == 301:
        ans = -1

    print(ans)


