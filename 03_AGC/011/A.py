from sys import stdin
def input():
    return stdin.readline().rstrip("\n")

n, c, k = map(int, input().split())
tl = [int(input()) for i in range(n)]
tl.sort()
tl.append(10 ** 18)
ans = 0
lim = tl[0] + k
cap = c
for t in tl:
    if t > lim or cap == 0:
        ans += 1
        lim = t + k
        cap = c
    cap -= 1
print(ans)





