

if __name__ == '__main__':
    S = input()
    T = input()

    len_S = len(S)
    len_T = len(T)

    dp = [[0]*(len_S+1) for _ in range(len_T+1)]

    for i in range(1, len_T+1):
        for j in range(1, len_S+1):
            if S[j-1] == T[i-1]:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]+1)
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    print(dp[len_T][len_S])



