A, B, K = map(int, input().split())
All = []
for i in range(min(A, B), 0, -1):
    if A % i == 0 and B % i == 0:
        All.append(i)

print(All[K-1])