

if __name__ == '__main__':
    N, X, T = map(int, input().split())
    if N % X == 0:
        ans = (N // X) * T
    else:
        ans = (N // X + 1)  * T

    print(ans)