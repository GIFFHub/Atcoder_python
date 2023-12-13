if __name__ == '__main__':
    N = int(input())
    S = input()
    K = 10**9 + 7
    Target = 'atcoder'
    len_target = len(Target)

    # dp[i][j] : Sのi文字目までで、Targetのj文字目の文字列を構成する場合の数

    dp = [[0 for _ in range(len_target+1)] for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(len_target+1):
            dp[i][j] += dp[i-1][j]
            if S[i-1] == Target[j-1] and j-1 >= 0:
                dp[i][j] += dp[i-1][j-1]
            dp[i][j] %= K

    print(dp[-1][-1])


