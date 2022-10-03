

N, M = map(int, input().split())

tmp = 1
ans = -1
flg = True
while flg:
    X = M*tmp
    if X < 10**N:
        ans = X
        tmp += 1
    else:
        flg = False

print(ans)