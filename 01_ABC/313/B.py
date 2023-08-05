

if __name__ == '__main__':
    N, M = map(int, input().split())
    A = []
    B = []
    d = dict()
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
        if b in d:
            d[b].append(a)
        else:
            d[b] = [a]

    cnt = 0
    saikyo = 0
    for i in range(1, N+1):
        if i not in d:
            cnt += 1
            saikyo = i

    if cnt == 1:
        print(saikyo)
    else:
        print(-1)



