N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp_A = [False]*N
dp_B = [False]*N

dp_A[0] = True
dp_B[0] = True


for i in range(1, N):
    if dp_A[i-1]:
        if abs(A[i] - A[i-1]) <= K:
            dp_A[i] = True
        if abs(B[i] - A[i-1]) <= K:
            dp_B[i] = True
    if dp_B[i-1]:
        if abs(A[i] - B[i-1]) <= K:
            dp_A[i] = True
        if abs(B[i] - B[i-1]) <= K:
            dp_B[i] = True

if dp_A[N-1] or dp_B[N-1]:
    print('Yes')
else:
    print('No')
