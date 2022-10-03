

if __name__ == '__main__':
    N, W = map(int, input().split())
    w = [0]
    v = [0]

    for _ in range(N):
        w_tmp, v_tmp = map(int, input().split())
        w.append(w_tmp)
        v.append(v_tmp)

    # dp[i][j] : i番目の品物まで入れられる時,重さjの時の最大価値
    # dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]]+v[i])
    dp = [[None]*(W+1) for _ in range(N+1)]

    for i in range(N+1):
        dp[i][0] = 0

    for j in range(W+1):
        dp[0][j] = 0


    for i in range(1, N+1):
        for j in range(1, W+1):
            if j-w[i] >= 0:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i])
            else:
                dp[i][j] = dp[i-1][j]

    ans = 0
    for j in range(W+1):
        ans = max(ans, dp[N][j])

    print(ans)

