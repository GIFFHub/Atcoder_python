

if __name__ == '__main__':
    S, T = input().split()
    A, B = map(int, input().split())
    U = input()

    d = dict()
    d[S] = A
    d[T] = B
    d[U] -= 1

    print(d[S], d[T])

