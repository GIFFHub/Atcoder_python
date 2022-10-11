
N, Q = map(int, input().split())
pos = list(range(1, N+1))

for _ in range(Q):
    x = pos.index(int(input()))
    x1 = x % N
    if x+1 == N:
        x2 = (x-1) % N
    else:
        x2 = (x+1) % N
    pos[x2], pos[x1] = pos[x1], pos[x2]

print(pos[0], end='')

for i in range(1, N):
    print(' %d' % pos[i], end='')

