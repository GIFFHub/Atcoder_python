def check(m, d):
    m = str(m)
    d = str(d)
    s = set()
    for k in m:
        s.add(k)
    for k in d:
        s.add(k)

    if len(s) == 1:
        return True
    else:
        return False


if __name__ == '__main__':
    N = int(input())
    D = list(map(int, input().split()))

    ans = 0
    for i in range(1, N+1): # 月
        for j in range(1, D[i-1]+1): # 日
            if check(i, j):
                ans += 1

    print(ans)

