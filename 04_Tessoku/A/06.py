

N, Q = map(int, input().split())

A = list(map(int, input().split()))

cum_A = [0]
tmp = 0
for a in A:
    tmp += a
    cum_A.append(tmp)

for _ in range(Q):
    L, R = map(int, input().split())
    print(cum_A[R]-cum_A[L-1])





