from collections import deque

if __name__ == '__main__':
    N1, N2, M = map(int, input().split())

    N = N1 + N2

    # 隣接リストの作成
    G = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    # 幅優先探索の初期化
    dist = [-1] * (N+1)
    dist[1] = 0

    Q = deque()
    Q.append(1)

    # 幅優先探索
    while len(Q) >= 1:
        pos = Q.popleft()
        for nex in G[pos]:
            if dist[nex] == -1:
                dist[nex] = dist[pos] + 1
                Q.append(nex)

    T1 = max(dist)

    # 幅優先探索の初期化
    dist = [-1] * (N+1)
    dist[N] = 0

    Q.append(N)
    # 幅優先探索
    while len(Q) >= 1:
        pos = Q.popleft()
        for nex in G[pos]:
            if dist[nex] == -1:
                dist[nex] = dist[pos] + 1
                Q.append(nex)

    T2 = max(dist)
    ans = T1 + T2 + 1

    print(ans)

