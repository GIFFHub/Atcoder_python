

if __name__ == '__main__':
    N, P, Q, R, S = map(int, input().split())
    A = list(map(int, input().split()))

    A1 = A[:P-1]
    A2 = A[P-1:Q]
    A3 = A[Q:R-1]
    A4 = A[R-1:S]
    A5 = A[S:]

    ans = A1 + A4 + A3 + A2 + A5

    print(*ans)