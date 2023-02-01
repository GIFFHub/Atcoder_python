import itertools

if __name__ == '__main__':
    N, W = map(int, input().split())
    S = []
    T = []
    P = []
    for _ in range(N):
        s, t, p = map(int, input().split())
        S.append(s)
        T.append(t)
        P.append(p)

    M = max(T)+1

    K = [0]*M
    for i in range(N):
        K[S[i]] += P[i]
        K[T[i]] -= P[i]

    K_crr = itertools.accumulate(K)

    for k in K_crr:
        if k > W:
            print('No')
            break
    else:
        print('Yes')



