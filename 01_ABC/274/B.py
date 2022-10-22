H, W = map(int, input().split())

C = []
for _ in range(H):
    C.append(input())


for i in range(W):
    cnt = 0
    for j in range(H):
        if C[j][i] == '#':
            cnt += 1
    if i == 0:
        print('%d' % cnt, end='')
    else:
        print(' %d' % cnt, end='')

