

if __name__ == '__main__':
    '''
    dp[i][j] : (i+1)枚目のカードまで使ったときに合計がjになるかならないか
    dp[i][j] が True になるのは以下２パターン
      ・dp[i-1][j] = Trueの場合（A[i]を追加せずとも、合計Sにできる場合）
      ・dp[i-1][j-A[i]] = Trueの場合（A[i]を追加することで、ちょうど合計Sになる場合）
    0 <= i <= N - 1
    0 <= j <= S    
    
    '''
    N, S = map(int, input().split())
    A = list(map(int, input().split()))

    dp = [[None]*(S+1) for x in range(N+1)]
    # dp[0][A[0]] = True
    dp[0][0] = True

    for i in range(1, S+1):
        dp[0][i] = False

    for i in range(1, N+1):
        for j in range(S+1):
            if j-A[i-1] < 0:
                if dp[i-1][j]:
                    dp[i][j] = True
                else:
                    dp[i][j] = False
            else:
                if dp[i-1][j] or dp[i-1][j-A[i-1]]:
                    dp[i][j] = True
                else:
                    dp[i][j] = False

    if dp[N][S]:
        print('Yes')
    else:
        print('No')



