N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_max = max(A)

flg = 0
for b in B:
    if A[b-1] == A_max:
        flg = 1

if flg:
    print('Yes')
else:
    print('No')

