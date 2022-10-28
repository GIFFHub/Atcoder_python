N, M = map(int, input().split())
S = list(input().split())
T = list(input().split())

cnt = 0
for s in S:
    if s == T[cnt]:
        print('Yes')
        cnt += 1
    else:
        print('No')

