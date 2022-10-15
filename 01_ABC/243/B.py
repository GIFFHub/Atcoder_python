N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_set = set(A)
B_set = set(B)

ans1 = 0
ans2 = 0
for i in range(N):
    if A[i] == B[i]:
        ans1 += 1
    elif A[i] in B_set:
        ans2 += 1

print(ans1)
print(ans2)

