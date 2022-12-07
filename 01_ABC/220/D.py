'''
・問題
　・配列Aがあり、先頭2つを足した10の余り or 先頭2つをかけた10の余り
　　で置き換える
　・配列要素が1つになるまで、上記操作のどちらかを行う
　・全操作パターンで、最後の要素が0~9になるのは何回か？

・気づきメモ
　・全パターンやってたらTLE
　・１パターンの操作回数はN-1回
　・左2つの要素の1つが0になったら、x✖️yは0


・方針
　・配るDPで解く
　・dp[i][j] : i番目の要素がjになる場合の数

'''


def operation_f(x, y):
    return (x+y) % 10


def operation_g(x, y):
    return (x*y) % 10


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    dp = [[0]*10 for _ in range(N)]

    # 0番目の要素はA[0]にしかならないのでそれだけ場合の数は1
    dp[0][A[0]] = 1

    for i in range(N-1):
        for j in range(10):
            dp[i+1][operation_f(j, A[i+1])] += dp[i][j] % MOD
            dp[i+1][operation_g(j, A[i+1])] += dp[i][j] % MOD

    for ans in dp[N-1]:
        print(ans % MOD)




