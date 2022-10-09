

N, W = map(int, input().split())
A = list(map(int, input().split()))
A.append(0)
A.append(0)
A.sort()
A_set = set(A)
ans_set = set()
ans = 0
max_index = N+2
for i in range(N):
    if A[i] >= W:
        max_index = i
        break

for i in range(max_index):
    for j in range(i+1, max_index):
        for k in range(j+1, max_index):
            tmp = A[i]+A[j]+A[k]
            if tmp > W:
                break
            ans_set.add(tmp)

print(len(ans_set))
