

if __name__ == '__main__':
    N, X = map(int, input().split())

    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    '''
    dp[i][j] : i種類目までの硬貨を使っていい時、合計金額をjにできるか
    
    '''

    dp = [[False]*(X+1) for _ in range(N+1)]

    for i in range(N+1):
        for j in range(X+1):
            if j == 0:
                dp[i][j] = True

            if i > 0:
                if dp[i-1][j]:
                    dp[i][j] = True

            if dp[i][j]:
                if i < N:
                    for b in range(1, B[i]+1):
                        if j+A[i]*b <= X:
                            if i <= N-1:
                                dp[i+1][j+A[i]*b] = True

    if dp[N][X]:
        print('Yes')
    else:
        print('No')



