
def give_red(n):
    if n == 1:
        return 0
    else:
        return give_red(n-1) + X * give_blue(n)


def give_blue(n):
    if n == 2:
        return Y
    else:
        return give_red(n-1) + Y * give_blue(n-1)


if __name__ == '__main__':
    N, X, Y = map(int, input().split())
    ans = 0
    print(give_red(N))