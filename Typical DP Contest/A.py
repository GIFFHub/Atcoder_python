
if __name__ == '__main__':
    N = int(input())
    P = list(map(int, input().split()))

    dp = [[0 for _ in range(N*100+1)] for _ in range(N)]

    # DP[i][j]:i番目までのテストでj点とることができるか（できる：1、できない：0）
    dp[0][0] = 1 # 何番目までのテストであっても0点は取れる
    dp[0][P[0]] = 1
    for i in range(N):
        for j in range(N*100+1):
            if dp[i-1][j] == 1:
                dp[i][j] = 1
            elif j-P[i] >= 0:
                if dp[i-1][j-P[i]] == 1:
                    dp[i][j] = 1
    print(sum(dp[-1]))





