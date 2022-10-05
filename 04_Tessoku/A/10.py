
N = int(input())

A = list(map(int, input().split()))

D = int(input())

max_left = [A[0]]
max_right = [A[N-1]]

for i in range(1, N):
    max_left.append(max(A[i], max_left[i-1]))
    max_right.append(max(A[(N-1)-i], max_right[i-1]))


for _ in range(D):
    l, r = map(int, input().split())
    print(max(max_left[l-2], max_right[N-r-1]))




