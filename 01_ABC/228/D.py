

if __name__ == '__main__':
    Q = int(input())
    T = []
    X = []
    N = 2**20
    A = [-1]*N

    for _ in range(Q):
        t, x = map(int, input().split())

        if t == 1:
            h = x
            while True:
                if A[h % N] != -1:
                    h += 1
                else:
                    A[h % N] = x
                    break

        elif t == 2:
            print(A[x % N])

