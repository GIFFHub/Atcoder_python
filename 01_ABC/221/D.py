from collections import defaultdict

N = int(input())
A = []
B = []

# ログイン人数に変動がある日の集合
X = set()
d_in = defaultdict(int)
d_out = defaultdict(int)

for _ in range(N):
    a, b = map(int, input().split())
    X.add(a)
    X.add(a + b)
    d_in[a] += 1
    d_out[a + b] += 1

X = list(X)
X.sort()
ans = [0] * len(X)

for i in range(len(X)):
    ans[i] += d_in[X[i]]
    ans[i] -= d_out[X[i]]

ans_crr = []
tmp = 0
for a in ans:
    tmp += a
    ans_crr.append(tmp)

d_ans = dict()

for j in range(len(ans_crr)):
    if ans_crr[j] in d_ans:
        d_ans[ans_crr[j]].append(j)
    else:
        d_ans[ans_crr[j]] = [j]

ans_ks = []
for k in range(1, N + 1):
    ans_k = 0
    if k in d_ans:
        for t in d_ans[k]:
            ans_k += X[t + 1] - X[t]
    ans_ks.append(ans_k)

print(*ans_ks)


