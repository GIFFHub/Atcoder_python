from collections import deque

if __name__ == '__main__':
    N, M = map(int, input().split())

    # (0,0)からどのマスに移動できるか調べる。
    # つまり(i,j)から相対的にどこに移動できるかわかるようになる。
    D = []
    for dx in range(-(N-1), N):
        for dy in range(-(N-1), N):
            if dx**2 + dy**2 == M:
                D.append([dx, dy])

    # 最小移動距離行列
    INF = 1<<62
    G = [[INF]*N for _ in range(N)]
    G[0][0] = 0
    # DFSはdequeで実装
    dq = deque([(0, 0, 0)])

    # dequeが空になるまで
    while dq:
        t, x, y = dq.popleft()
        for dx, dy in D:
            xn = x+dx
            yn = y+dy
            # (xn,yn)が枠内かどうか
            if 0 <= xn < N and 0 <= yn < N:
                # t:移動回数が最小かどうか
                if G[xn][yn] > t+1: # t+1 が、今回(xn,yn)に至る移動回数
                    G[xn][yn] = t+1
                    dq.append((t+1, xn, yn)) # 最小移動回数として、更新

    for x in range(N):
        for y in range(N):
            if G[x][y] == INF:
                G[x][y] = -1

    for g in G:
        print(*g)





