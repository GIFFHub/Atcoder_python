

N, M = map(int, input().split())

table = [[False]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == j:
            table[i][j] = True

for _ in range(M):
    buto = list(map(int, input().split()))
    for k in range(1, len(buto)):
        for l in range(k+1, len(buto)):
            table[buto[k]-1][buto[l]-1] = True
            table[buto[l]-1][buto[k]-1] = True

for i in range(N):
    for j in range(N):
        if table[i][j] == False:
            print('No')
            exit()
print('Yes')
