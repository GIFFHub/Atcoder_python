

if __name__ == '__main__':
    N = int(input())
    A = []
    B = []
    mod = 998244353
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    # dp[i][j] : j番目にi側を選んだ場合の場合の和

    dp = [[0, 0] for _ in range(N)]
    dp[0] = [1, 1]
    for i in range(1, N):
        if A[i] != A[i-1]:
            dp[i][0] += dp[i-1][0]
        if A[i] != B[i-1]:
            dp[i][0] += dp[i-1][1]
        if B[i] != A[i-1]:
            dp[i][1] += dp[i-1][0]
        if B[i] != B[i-1]:
            dp[i][1] += dp[i-1][1]
        dp[i][0] %= mod
        dp[i][1] %= mod

    ans = dp[-1][0] + dp[-1][1]
    ans %= mod
    print(ans)


