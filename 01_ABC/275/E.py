from fractions import Fraction

def func(x, k):
    '''
    xのk乗を高速で返します
    :param x:
    :param k:
    :return: x**k
    '''




if __name__ == '__main__':
    N, M, K = map(int, input().split())
    T = 998244353

    # dp[i][j] : ルーレットをi回回した時、j地点にいる確率

    dp = [[0 for j in range(N+1)] for i in range(K+1)]
    dp[0][0] = 1

    for i in range(1, K+1):
        for j in range(1, N+1):
            for k in range(1, M+1):
                if j-k >= 0:
                    dp[i][j] += dp[i-1][j-k] * (1/M)
                if j+k > N and j+k-N >= 0:
                    dp[i][j] += dp[i-1][j+k-N] * (1/M)

    ans = 0
    for i in range(K+1):
        ans += dp[i][N]
    '''
    ans = Fraction(ans)
    ans_nume = ans.numerator
    ans_demo = ans.denominator

    a = ans_nume % T
    b = ans_demo % T
    '''
    #print((a*(b**(T-2))) % T)
    print(divmod(ans, T))




