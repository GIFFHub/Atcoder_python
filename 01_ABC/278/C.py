
if __name__ == '__main__':
    N, Q = map(int, input().split())
    T = []
    A = []
    B = []
    d = dict()
    r = set()
    for _ in range(Q):
        t, a, b = map(int, input().split())

        if t == 1:
            if a in r:
                d[a].add(b)
            else:
                d[a] = set()
                d[a].add(b)
                r.add(a)
        elif t == 2:
            if a in r:
                if b in d[a]:
                    d[a].remove(b)
            else:
                pass
        elif t == 3:
            if a in r and b in r:
                if a in d[b] and b in d[a]:
                    print('Yes')
                else:
                    print('No')
            else:
                print('No')



