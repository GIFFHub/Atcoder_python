import sys


def check(l):
    for n in l:
        if not learn[n-1]:
            learn[n-1] = True
            if table[n-1][1] != 0:
                check(table[n-1][2:])
    return


if __name__ == '__main__':
    N = int(input())
    table = [[]for _ in range(N)]
    learn = [False]*N
    learn[N-1] = True
    sys.setrecursionlimit(2000000)
    for i in range(N):
        table[i] = list(map(int, input().split()))

    '''
    考察
    ・学ぶべきは、N番目の事前学習要素
    ・N番目の事前学習要素をいかに短時間で学ぶか
    ・どのみち事前学習要素は学ばないといけない
    ・学ぶ必要のないものはどれかを見極める？
    ・table[N-1][3:]から木構造で、たどり着くもの全て上げる問題
    '''

    need = table[N-1][2:]
    check(need)
    ans = 0
    for j in range(N):
        if learn[j]:
            ans += table[j][0]

    print(ans)

