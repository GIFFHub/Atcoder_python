

if __name__ == '__main__':
    N, M, K = map(int, input().split())
    T = 998244353
    # dp[i][j]: i項目の値がjである場合の和
    dp = [[0] * M for _ in range(N)]

    # 1項目は全て1通り
    for j in range(M):
        dp[0][j] = 1

    # 2項目以降
    for i in range(N-1):
        S = sum(dp[i])
        P = [0]*M
        P[0] = sum(dp[i][:K])
        dp[i+1][0] = (S-P[0]) % T
        for j in range(1, M):
            P[j] = P[j-1]
            if j+K-1 <= M-1:
                P[j] += dp[i][j+K-1]
            if j-K >= 0:
                P[j] -= dp[i][j-K]
            dp[i+1][j] = (S - P[j]) % T

    ans = sum(dp[N-1])
    ans %= T
    print(ans)

