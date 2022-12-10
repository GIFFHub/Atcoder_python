

if __name__ == '__main__':
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A_r = []
    for a in A:
        A_r.append(a % D)

    # dp[i][j][x] = i項目まで、j項選んだ時、Dで割ったあまりがxになる和の最大値
    dp = [[[-1]*D for _ in range(K+1)] for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, K+1):
            if i < j:
                break
            for x in range(D):
                # A[i]が今回考慮に追加されたもの
                if i == j:
                    tmp = sum(A_r[:i])
                    if tmp % D == x:
                        dp[i][j][x] = sum(A[:i])

                else:
                    # A[i]を使わないパターン
                    dp[i][j][x] = max(dp[i][j][x], dp[i-1][j][x])
                    # A[i]を使って、他の項1つ減らすパターン
                    if j == 1 and A[i-1]%D == x:
                        dp[i][j][x] = A[i-1]

                    elif dp[i-1][j-1][(D+x-A_r[i-1]) % D] != -1:
                        dp[i][j][x] = max(dp[i][j][x], dp[i-1][j-1][(D+x-A_r[i-1]) % D]+A[i-1])

    print(dp[N][K][0])

