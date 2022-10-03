

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # dp[i] : i番目の部屋にいくために必要な最小移動時間

    dp = [10**7+1]*N
    dp[0] = 0
    dp[1] = A[0]

    for i in range(2, N):
        dp[i] = min(dp[i-1]+A[i-1], dp[i-2]+B[i-2])

    print(dp[N-1])
