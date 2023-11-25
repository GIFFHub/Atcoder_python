

if __name__ == '__main__':
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))

    for i in range(N):
        if L <= A[i] <= R:
            uhen = 0
            X = A[i]
        else:
            uhen = min(abs(L - A[i]), abs(R - A[i]))
            X = uhen + A[i]
            if X > R:
                X = R
            elif X < L:
                X = L

        print(X)
