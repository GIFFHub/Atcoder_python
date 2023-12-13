def dfs(point, cnt):
    if dist[point] >= 0:
        return
    else:
        dist[point] = cnt
        nxts = d[point]
        for nxt in nxts:
            if dist[nxt] >= 0:
                dfs(nxt, cnt+1)
    return


import sys

sys.setrecursionlimit(20000000)

if __name__ == '__main__':
    N = int(input())
    d = dict()
    for _ in range(N-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        if a in d:
            d[a].append(b)
        else:
            d[a] = [b]
        if b in d:
            d[b].append(a)
        else:
            d[b] = [a]
    dist = [-1] * N
    dfs(0, 0)

    T0 = []
    T1 = []
    for i in range(N):
        if dist[i] % 2 == 0:
            T0.append(i+1)
        else:
            T1.append(i+1)
    if len(T0) > len(T1):
        print(*T0[:N//2])
    else:
        print(*T1[:N//2])




