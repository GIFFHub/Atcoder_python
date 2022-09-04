


if __name__ == '__main__':
    N, K = map(int, input().split())
    h = list(map(int, input().split()))

    dp = [10000*N for i in range(N)]

    dp[0] = 0 # 初期値に至るコストは0

    for i in range(1, N): # 現在地ループ
        for j in range(1, K+1): # どれだけ戻るかループ
            if i-j >= 0: # 初期値より戻らないように
                prev_dp = dp[i-j]
                cost = abs(h[i]-h[i-j])
                current_dp = dp[i]
                dp[i] = min(prev_dp + cost, current_dp)
    print(dp[N-1])


