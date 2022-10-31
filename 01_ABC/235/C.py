

if __name__ == '__main__':
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    K = []
    d = dict()
    s = set()

    for i, a in enumerate(A):
        if a in s:
            d[a].append(i+1)
        else:
            d[a] = [i+1]
            s.add(a)

    for _ in range(Q):
        x, k = map(int, input().split())
        if x in s:
            if len(d[x]) >= k:
                print(d[x][k-1])
            else:
                print(-1)
        else:
            print(-1)
