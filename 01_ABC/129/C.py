
if __name__ == '__main__':
    N, M = map(int, input().split())
    A = set()
    mod = 1000000007
    for _ in range(M):
        A.add(int(input()))

    dp = [0] * (N+1)
    dp[0] = 1
    for i in range(1, N+1):
        if i in A:
            continue
        if i > 1:
            dp[i] = dp[i-1]+dp[i-2]
        else:
            dp[i] = dp[i-1]
        dp[i] %= mod

    print(dp[-1])

