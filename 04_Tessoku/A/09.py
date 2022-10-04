
H, W, N = map(int, input().split())
table = [[0 for _ in range(W)] for _ in range(H)]
for i in range(N):
    a, b, c, d = map(int, input().split())
    table[a-1][b-1] += 1
    if c < H:
        table[c][b-1] -= 1
    if d < W:
        table[a-1][d] -= 1
    if c < H and d < W:
        table[c][d] += 1

cum = [[0 for _ in range(W)] for _ in range(H)]

tmp = 0
for j in range(H):
    for k in range(W):
        tmp += table[j][k]
        cum[j][k] = tmp
    tmp = 0

for j in range(1, H):
    for k in range(W):
        tmp += cum[j-1][k]
        cum[j][k] += tmp
        tmp = 0

for j in range(H):
    for k in range(W):
        if k == 0:
            print(cum[j][k], end='')
        else:
            print(' %d' % cum[j][k], end='')
    print()


