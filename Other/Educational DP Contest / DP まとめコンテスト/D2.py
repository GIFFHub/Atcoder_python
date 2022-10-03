

if __name__ == '__main__':
    N, W = map(int, input().split())
    w = []
    v = []
    for _ in range(N):
        tmp_w, tmp_v = map(int, input().split())
        w.append(tmp_w)
        v.append(tmp_v)

    dp = [[0 for _ in range(W+1)] for _ in range(N)]

    for i in range(N): # i：個数-1（インデックス）
        for j in range(W+1): # j：重さ-1（インデックス）
            if j-w[i] >= 0:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]]+v[i])
            else:
                dp[i][j] = dp[i-1][j]
    # print(dp)
    print(dp[-1][-1])




