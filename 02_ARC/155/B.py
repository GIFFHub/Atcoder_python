

if __name__ == '__main__':
    Q, A, B = map(int, input().split())
    s = set()
    s.add((A, B))
    for _ in range(Q):
        t, a, b = map(int, input().split())

        if t == 1:
            s.add((a, b))
        if t == 2:


