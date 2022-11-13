

if __name__ == '__main__':
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    dp = [[None]*N for _ in range(M)]
    max_tmp = -2*(10**5)-1
    for index, a in enumerate(A):
        max_tmp = max(max_tmp, a)
        dp[0][index] = max_tmp


    for i in range(1, M):
        max_tmp = -2 * (10 ** 5) - 1
        for j in range(i, N):
            dp[i][j] = max(max_tmp, dp[i-1][j-1]+(i+1)*A[j])
            max_tmp = dp[i][j]

    #print(dp)
    print(dp[M-1][N-1])


