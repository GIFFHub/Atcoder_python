def checkfront(x):


if __name__ == '__main__':
    N, Q = map(int, input().split())
    d_front = dict()
    d_back = dict()
    for _ in range(Q):
        query = list(map(int, input().split()))

        if query[0] == 1:
            d_back[query[1]] = query[2]
            d_front[query[2]] = query[1]

        elif query[0] == 2:
            d_back[query[1]] = None
            d_front[query[2]] = None

        elif query[0] == 3:
            while True:
                d_front[query[1]]

