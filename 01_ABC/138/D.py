from collections import defaultdict
import sys
sys.setrecursionlimit(50000000)


def dfs(prev, curr, point):
    global ans
    ans[curr-1] = point
    nxts = d[curr]
    for nxt in nxts:
        if not nxt == prev:
            if nxt in P:
                dfs(curr, nxt, point+P[nxt])
            else:
                dfs(curr, nxt, point)


if __name__ == '__main__':
    N, Q = map(int, input().split())
    d = dict()
    ans = [0] * N
    for i in range(N-1):
        a, b = map(int, input().split())
        if a in d:
            d[a].append(b)
        else:
            d[a] = [b]
        if b in d:
            d[b].append(a)
        else:
            d[b] = [a]

    P = defaultdict(int)
    for j in range(Q):
        p, x = map(int, input().split())
        P[p] += x
    root_point = 0
    if 1 in P:
        root_point += P[1]
    dfs(0, 1, root_point)
    print(*ans)

