A, B, C, X = map(int, input().split())
ans = 0
if X <= A:
    ans = 1
elif A < X <= B:
    ans = C/(B-A)
else:
    ans = 0

print(ans)
