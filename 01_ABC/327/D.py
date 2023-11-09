import sys
sys.setrecursionlimit(10**7)


def dfs(current_pos):
    global ans
    nxts = d[current_pos]

    for nxt in nxts:
        if past[nxt] is None:
            if past[current_pos]:
                past[nxt] = False
            else:
                past[nxt] = True
            dfs(nxt)
        else:
            if past[current_pos] == past[nxt]:
                ans = 1
    return


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    d = dict()
    ans = 0 # 0:良い数列の組がある（可能性あり） # 1: 良い数列の組みはない

    # 二部グラフ問題として考える

    # 隣接リスト
    for i in range(M):
        a = A[i] - 1
        b = B[i] - 1

        if a in d:
            d[a].append(b)
        else:
            d[a] = [b]

        if b in d:
            d[b].append(a)
        else:
            d[b] = [a]

    # 二部グラフ判定
    past = [None] * N
    for j in range(N):
        if past[j] is None:
            past[j] = True
            if j in d:
                dfs(j)

    if ans == 0:
        print('Yes')
    else:
        print('No')















