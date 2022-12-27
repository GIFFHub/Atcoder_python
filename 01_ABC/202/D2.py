

def find_kth(A, B, K):
    '''
    :param A: aがあと何個残っているか
    :param B: bがあと何個残っているか
    :param K: 辞書順
    :return: 文字列
    '''

    # aが残ってない→bしかない
    if A == 0:
        return 'b' * B

    if B == 0:
        return 'a' * A

    # aを先頭とした場合に、その文字列の辞書順がKより大きい
    # →先頭がaである文字列郡の中にK番目の文字列はある
    if K <= dp[A-1][B]:
        return 'a' + find_kth(A-1, B, K)

    # 先頭がbである文字列郡の中に、K番目の文字列がある場合
    else:
        return 'b' + find_kth(A, B-1, K-dp[A-1][B])






if __name__ == '__main__':
    A, B, K = map(int, input().split())

    '''
    dp[i][j] : i個のaとj個のbからなる、文字列の場合の和
    '''

    dp = [[0]*(B+1) for _ in range(A+1)]
    dp[0][0] = 1

    for i in range(0, A+1):
        for j in range(0, B+1):
            if i > 0:
                dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i][j-1]

    print(find_kth(A, B, K))









