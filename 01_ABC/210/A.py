

if __name__ == '__main__':
    N, A, X, Y = map(int, input().split())

    if N <= A:
        ans = X * N
    else:
        ans = X * A + Y * (N-A)

    print(ans)