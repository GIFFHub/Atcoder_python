

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    M = max(B)
    ans = 0
    T = 998244353
    dp = [[0]*(M+1) for _ in range(N)]
    tmp_crr = [0]*(M+2)
    tmp = 0
    for j in range(A[0], M+1):
        if j <= B[0]:
            dp[0][j] = 1
            tmp += 1
        tmp_crr[j+1] = tmp

    for i in range(1, N):
        for j in range(A[i], B[i]+1):
            dp[i][j] = tmp_crr[j+1] - tmp_crr[A[i-1]]
            dp[i][j] %= T
        tmp_crr = [0]*(M+2)
        tmp = 0
        for j in range(A[i], M+1):
            tmp += dp[i][j]
            tmp_crr[j+1] = tmp % T

    #ans = sum(dp[N-1])
    ans = sum(dp[N-1]) % T

    print(ans)


