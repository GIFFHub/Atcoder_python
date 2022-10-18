N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(M):
    if B[i] in A:
        A.remove(B[i])
        continue
    else:
        print('No')
        break
else:
    print('Yes')