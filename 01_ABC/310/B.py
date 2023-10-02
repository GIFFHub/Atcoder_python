

if __name__ == '__main__':
    N, M = map(int, input().split())
    P = []
    C = []
    F = []
    for _ in range(N):
        X = list(map(int, input().split()))
        P.append(X[0])
        C.append(X[1])
        F.append(X[2:])

    for i in range(N):
        for j in range(N):
            if i == j:
                continue

            if P[i] >= P[j]:
                pass
            else:
                continue

            for fi in F[i]:
                if fi in F[j]:
                    pass
                else:
                    break
            else:
                if P[i] > P[j]:
                    print('Yes')
                    exit()
                else:
                    flg = False
                    for fj in F[j]:
                        if fj in F[i]:
                            pass
                        else:
                            flg = True
                    if flg:
                        print('Yes')
                        exit()
                    else:
                        continue

    print('No')

