def g1(x):
    x = list(str(x))
    x.sort(reverse=True)
    x = ''.join(x)
    x = int(x)
    return x


def g2(x):
    x = list(str(x))
    x.sort()
    i = 0
    for t in x:
        if t == 0:
            i += 1
        else:
            break

    x = ''.join(x[i:])
    x = int(x)
    return x


def f(x):
    return g1(x) - g2(x)


if __name__ == '__main__':
    N, K = map(int, input().split())

    a = N

    for i in range(K):
        a = f(a)

    print(a)