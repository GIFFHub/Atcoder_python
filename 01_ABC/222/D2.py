

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    T = 998244353
    dp = [[0]*(N+1) for _ in range(max(B)+1)]

    for i in range(A[0], B[0]+1):
        dp[i][1] = 1
    for i in range(1, max(B)+1):
        for j in range(1, N):
            up = max(i, A[j])
            down = B[j]
            for k in range(up, down+1):
                dp[k][j+1] += dp[i][j]
                dp[k][j+1] %= T

    for i in range(max(B)+1):
        ans += dp[i][-1]
        ans %= T
    print(ans)




