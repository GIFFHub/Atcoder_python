import sys
sys.setrecursionlimit(50000000)


def find_kth(A, B, K):
    # A == 0のとき→aが一つもない→全てb→辞書順で何番目でも同じbbbbbbb
    if A == 0:
        return 'b' * B

    # B == 0のとき→bが一つもない→全てb→辞書順で何番目でも同じaaaaaaa
    if B == 0:
        return 'a' * A

    # 先頭をaとした場合の残り（A-1個のaとB個のbの全通り）がKより大きい場合
    # → K番目を含んでいる
    # → 先頭はa
    # → 再帰でもう一度探す
    if K <= dp[A - 1][B]:
        return 'a' + find_kth(A - 1, B, K)

    # 先頭をaとした場合の残り（A-1個のaとB個のbの全通り）がKより小さい場合
    # → 先頭をaにするとK番目に届かない
    # → 先頭はb
    # → 再帰でもう一度探す
    else:
        return 'b' + find_kth(A, B - 1, K - dp[A - 1][B])


if __name__ == '__main__':
    A, B, K = map(int, input().split())
    MAX = 30
    # C(i, j): aがi個、bがj個からなる文字列の総数

    dp = [[0]*(B+1) for _ in range(A+1)]
    dp[0][0] = 1
    for i in range(0, A+1):
        for j in range(0, B+1):
            if i > 0:
                dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i][j-1]

    print(find_kth(A, B, K))
