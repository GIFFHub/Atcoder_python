from collections import deque

N, M = map(int, input().split())

# (0,0)から移動できる相対座標を求める
move = []
for dx in range(-(N-1), N):
    for dy in range(-(N-1), N):
        if dx**2 + dy**2 == M:
            move.append((dx, dy))

# 移動最短距離テーブルを初期化する
INF = 1<<62
min_move = [[INF]*N for _ in range(N)]
min_move[0][0] = 0

# DFS用のdequeを用意する
dq = deque([(0, 0, 0)])

# DFS
while dq:
    cnt, x, y = dq.popleft()
    for dx, dy in move:
        xn = x + dx
        yn = y + dy
        if 0 <= xn < N and 0 <= yn < N:
            if min_move[xn][yn] > cnt+1:
                min_move[xn][yn] = cnt+1
                dq.append((cnt+1, xn, yn))

for i in range(N):
    for j in range(N):
        if min_move[i][j] == INF:
            min_move[i][j] = -1


for m in min_move:
    print(*m)


