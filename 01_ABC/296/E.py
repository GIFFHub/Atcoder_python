from collections import defaultdict
from collections import deque
import sys
sys.setrecursionlimit(5000000)


def check(current):
    # 今回の調査ですでに出てきている点であればループ
    if current in s:
        dist[current] = -1
        return
    s.add(current)
    nxts = T[current]
    # 各次の点について
    for nxt in nxts:
        if nxt in s:
            dist[nxt] = -1
            dist[current] = -1
            break
        # nxtがループ点だったら
        if dist[nxt] == -1:
            # currentもループ点にする
            dist[current] = -1
            break
        elif nxt == current:
            dist[nxt] = -1
            dist[current] = -1
        else:
            # 行ったことあるなら
            if visit[nxt]:
                dist[current] = max(dist[current], dist[nxt] + 1)
            # 行ったことないなら
            else:
                visit[nxt] = True
                dist[nxt] = max(dist[nxt], dist[current] - 1)
                check(nxt)


    return




if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    # T[i] : 頂点iに移動できる点のリスト
    T = [[] for _ in range(N)]
    for i, a in enumerate(A):
        T[a-1].append(i)
    visit = [False] * N
    dist = [0] * N
    for j in range(N):
        s = set()
        check(j)
    ans = 0
    for x in range(N):
        if dist[x] == -1:
            ans += 1
        elif N <= dist[x]:
            ans += 1

    print(ans)






