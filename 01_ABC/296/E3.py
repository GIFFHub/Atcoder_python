n = int(input())
a = list(map(int, input().split()))

deg = [0] * n
# deg[i] : 点iに向かってくる点の数

ikeru = [[] for i in range(n)]
# ikeru[i] : 点iから行ける点のリスト

for i in range(n):
    deg[a[i] - 1] += 1
    ikeru[i].append(a[i] - 1)

mada = []
for i in range(n):
    if deg[i] == 0:
        mada.append(i)

while mada:
    i = mada.pop()
    for j in ikeru[i]:
        deg[j] -= 1
        if deg[j] == 0:
            mada.append(j)

ans = 0
for i in range(n):
    if deg[i] >= 1:
        ans += 1
print(ans)