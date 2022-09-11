
if __name__ == '__main__':
    N = int(input())
    P = list(map(int, input().split()))

    dp = [[0 for _ in range(N**2+1)] for _ in range(N)]
    ans = set()
    ans.add(0)
    # DP[i][j]:i番目までのテストでj点とることができるか（できる：1、できない：0）
    for i in range(N):
        for j in range(N**2+1):
            if j-P[i] >= 0:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-P[i]]+P[i])
            else:
                dp[i][j] = dp[i-1][j]
            ans.add(dp[i][j])


    print(len(ans))
