N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


pos = 0
for i in range(N):

    if i == 0:
        if max(A[i], B[i]) < K:
            pos = max(A[i], B[i])
        else:
            pos = min(A[i], B[i])
    else:
        if max(A[i], B[i]) - pos < K:
            pos = max(A[i], B[i])
        elif min(A[i], B[i]) - pos < K:
            print('No')
            exit()
        else:
            pos = min(A[i], B[i])

print('Yes')