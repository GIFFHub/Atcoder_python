

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
    sum_A = sum(A)
    sum_B = sum(B)

    dp = [[[301 for _ in range(sum_B+1)] for _ in range(sum_A + 1)] for _ in range(N + 1)]

    for i in range(N+1):
        for j in range(sum_A+1):
            for k in range(sum_B+1):
                if j == 0 and k == 0:
                    dp[i][j][k] = 0

    for i in range(1, N+1):
        for j in range(sum_A+1):
            for k in range(sum_B+1):
                if j-A[i-1] >= 0 and k-B[i-1] >= 0:
                    dp[i][j][k] = min(dp[i-1][j][k], dp[i-1][j-A[i-1]][k-B[i-1]]+1)

    ans = 301
    for i in range(1, N+1):
        for j in range(sum_A+1):
            for k in range(sum_B+1):
                if j >= X and k >= Y:
                    ans = min(ans, dp[i][j][k])

    if ans == 301:
        ans = -1

    print(ans)




