
N, A, B = map(int, input().split())

S = [['.']*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if (i+j)%2 == 1:
            S[i][j] = '#'
        S[i][j] *= B

for s in S:
    for _ in range(A):
        print(''.join(s))