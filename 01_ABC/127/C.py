

if __name__ == '__main__':
    N, M = map(int, input().split())
    L = 1
    R = N
    for i in range(M):
        l, r = map(int, input().split())
        L = max(L, l)
        R = min(R, r)

    print(max(0, R-L+1))
