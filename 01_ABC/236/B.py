N = int(input())
A = list(map(int, input().split()))

A.sort()
cnt = 0
ans = A[-1]
for i in range(len(A)-1):
    if A[i+1]==A[i]:
        cnt += 1
    else:
        if cnt != 3:
            ans = A[i]
            break
        cnt = 0

print(ans)
