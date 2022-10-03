

if __name__ == '__main__':
    N = int(input())
    h = list(map(int, input().split()))

    # dp[i] : i番目の足場に行ける最小のコスト

    dp = [None]*N
    dp[0] = 0
    dp[1] = abs(h[1]-h[0])

    for i in range(2, N):
        dp[i] = min(dp[i-1]+abs(h[i]-h[i-1]), dp[i-2]+abs(h[i]-h[i-2]))

    print(dp[N-1])
