

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    T = 998244353
    maxi = 3000
    '''
    dp[x][y] : c[x]がyになる場合の、c[x-1]までの場合の数
    
    '''
    dp = [[0]*maxi for _ in range(N)]

    for i in range(N):
        for j in range(maxi):
            if i == 0:
                if A[i] <= j+1 <= B[i]:
                    dp[i][j] = 1
            else:
                if A[i] <= j+1 <= B[i]:
                    dp[i][j] = sum(dp[i-1][:j+1]) % T

    ans = sum(dp[N-1]) % T

    print(ans)
