import numpy as np

if __name__ == '__main__':
    N, W = map(int, input().split())
    w = []
    v = []

    for _ in range(N):
        w_tmp, v_tmp = map(int, input().split())
        w.append(w_tmp)
        v.append(v_tmp)

    dp = [[0 for _ in range(W)] for _ in range(N)]

    for i in range(1,N):
        for j in range(W):
            if j-w[i] >= 0:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]]+v[i])
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[-1][-1])
