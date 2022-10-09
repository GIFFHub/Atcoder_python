from collections import deque

N, M = map(int, input().split())
A = []
B = []
for _ in range(M):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)


# 各頂点から移動できる頂点を調べる
move= [[] for _ in range(N)]
for i in range(M):
    move[A[i]-1].append(B[i])
    move[B[i]-1].append(A[i])

# 各頂点の最小移動辺数行列を作る
INF = 1<<63
table = [INF]*N
# 頂点1を起点とする
table[0] = 0

# DFS用のdeque作る(最小移動回数, 頂点番号)
dq = deque([(0, 1)])

# DFS
while dq:
    cnt, pos = dq.popleft()
    for next_pos in move[pos-1]:
        if table[next_pos-1] > cnt+1:
            table[next_pos-1] = cnt+1
            dq.append((cnt+1, next_pos))

for i in range(N):
    if table[i] == INF:
        table[i] = -1

for t in table:
    print(t)




