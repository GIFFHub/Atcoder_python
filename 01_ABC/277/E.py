

if __name__ == '__main__':

    # input
    N, M, K = map(int, input().split())
    U = []
    V = []
    A = []
    for _ in range(M):
        u, v, a = map(int, input().split())
        U.append(u)
        V.append(v)
        A.append(a)

    S = list(map(int, input().split()))

    # 隣接辞書表現
    T = dict()
    S = set()
    for _ in range(N):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        A.append(a)
        B.append(b)
        if a not in S:
            T[a] = [b]
        else:
            T[a].append(b)

        if b not in S:
            T[b] = [a]
        else:
            T[b].append(a)

        S.add(a)
        S.add(b)

