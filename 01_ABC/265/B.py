

if __name__ == '__main__':
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = set()
    Y = []

    for i in range(M):
        x, y = map(int, input().split())
        X.add(x)
        Y.append(y)

    pos = 0
    tmp = 0

    for i in range(N-1):
        if i+1 in X:
            T += Y[tmp]
            tmp += 1
        if T > A[i]:
            T -= A[i]

        else:
            print('No')
            break
    else:
        print('Yes')


