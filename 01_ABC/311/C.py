

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    route = [1]
    pos = 1
    s = set()
    s.add(1)

    while True:
        pos = A[pos-1]
        if pos in s:
            start = pos
            break
        else:
            s.add(pos)
        route.append(pos)

    flg = False
    ans = []
    for r in route:
        if flg:
            ans.append(r)
        if r == start:
            ans.append(start)
            flg = True

    print(len(ans))
    print(*ans)






