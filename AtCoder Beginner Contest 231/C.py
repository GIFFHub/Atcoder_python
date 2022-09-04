def binary_search(ng, ok, x):
    if ok - ng == 1:
        return ok
    cen = (ok+ng)//2

    if A[cen] >= x:
        return binary_search(ng, cen, x)
    else:
        return binary_search(cen, ok, x)


if __name__ == '__main__':
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    A = sorted(A)

    X = []
    for _ in range(Q):
        X.append(int(input()))

    ok_0 = N
    ng_0 = -1
    for i in range(Q):
        print(N - binary_search(ng_0, ok_0, X[i]))

