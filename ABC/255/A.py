

if __name__ == '__main__':

    X, A, D, N = map(int, input().split())
    S_max = A + N*D
    ans = 0
    if D > 0:
        if X >= S_max:
            ans = abs(X-S_max)

        elif X <= A:
            ans = abs(A-X)

        else:
            ans = min((X-A) % D, D//2)
    elif D <= 0:
        if X >= A:
            ans = abs(A-X)
        elif X <= S_max:
            ans = abs(X-S_max)
        else:
            ans = min(abs((X-S_max) % D), abs(D//2))

    print(ans)