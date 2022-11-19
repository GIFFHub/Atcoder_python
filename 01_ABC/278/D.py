from collections import defaultdict


if __name__ == '__main__':

    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    d = defaultdict(int)
    flg = False
    all_value = 0

    for _ in range(Q):
        query = list(map(int, input().split()))

        if query[0] == 1:
            all_value = query[1]
            d = defaultdict(int)
            flg = True

        elif query[0] == 2:
            d[query[1]] += query[2]

        elif query[0] == 3:
            if flg:
                print(all_value + d[query[1]])
            else:
                print(A[query[1]-1] + d[query[1]])

