import sys

sys.setrecursionlimit(20000000)


def dfs(pos, cnt):
    if dist[pos - 1] != -1:
        return
    else:
        dist[pos - 1] = cnt

    nxts = d[pos]
    for nxt in nxts:
        dfs(nxt, cnt+1)


if __name__ == '__main__':
    N = int(input())
    d = dict()
    for _ in range(N-1):
        a, b = map(int, input().split())
        if a in d:
            d[a].append(b)
        else:
            d[a] = [b]
        if b in d:
            d[b].append(a)
        else:
            d[b] = [a]

    u = 1
    dist = [-1] * N
    dfs(u, 0)

    v = dist.index(max(dist))+1

    dist = [-1] * N
    dfs(v, 0)

    print(max(dist)+1)





