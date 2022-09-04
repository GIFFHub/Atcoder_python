

if __name__ == '__main__':
    X, Y, N = map(int, input().split())

    if Y < 3*X:
        print(X * (N % 3) + Y * (N // 3))
    else:
        print(N * X)