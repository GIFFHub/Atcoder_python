import sys

sys.setrecursionlimit(200000)


def dfs(floor):
    global R
    # 行ったことある場合
    if floor in R:
        return
    else:
        R.add(floor)
        if floor in S:
            for i in range(len(T[floor])):
                dfs(T[floor][i])
    return


if __name__ == '__main__':
    N = int(input())
    A = []
    B = []

    # 隣接辞書表現
    T = dict()
    S = set()
    for _ in range(N):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        A.append(a)
        B.append(b)
        if a not in S:
            T[a] = [b]
        else:
            T[a].append(b)

        if b not in S:
            T[b] = [a]
        else:
            T[b].append(a)

        S.add(a)
        S.add(b)

    # 行ったことある階数かどうか集合
    R = set()

    dfs(0)

    print(max(R)+1)






