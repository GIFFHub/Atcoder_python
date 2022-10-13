N, K, X = map(int, input().split())

A = list(map(int, input().split()))
A.sort(reverse=True)

for i in range(N):
    k = A[i] // X
    if K >= k:
        A[i] -= k*X
        K -= k
    else:
        A[i] -= K*X
        K = 0
        break

if K == 0:
    print(sum(A))
else:
    A.sort(reverse=True)
    for i in range(N):
        if K > 0:
            A[i] = 0
            K -= 1
        else:
            break

    print(sum(A))
