

if __name__ == '__main__':
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    d = dict()
    d['r'] = P
    d['s'] = R
    d['p'] = S
    A = input()
    T = []
    for a in A:
        T.append(a)

    point = 0
    for i in range(N):
        if i >= K:
            if T[i] == T[i-K]:
                T[i] = 'x'
                continue
        point += d[T[i]]

    print(point)