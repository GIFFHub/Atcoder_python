H, W = map(int, input().split())
X = []
for _ in range(H):
    X.append(list(map(int, input().split())))

Q = int(input())

X_cum = [[0 for _ in range(W)] for _ in range(H)]
tmp = 0
for i in range(H):
    for j in range(W):
        tmp += X[i][j]
        X_cum[i][j] = tmp
        if i > 0:
            X_cum[i][j] += X_cum[i-1][j]
    tmp = 0

for _ in range(Q):
    a, b, c, d = map(int, input().split())
    x1 = x2 = x3 = x4 = 0
    x1 = X_cum[c-1][d-1]
    if a > 1:
        x2 = X_cum[a-2][d-1]
    if b > 1:
        x3 = X_cum[c-1][b-2]
    if a > 1 and b > 1:
        x4 = X_cum[a-2][b-2]
    print(x1 - x2 - x3 + x4)


