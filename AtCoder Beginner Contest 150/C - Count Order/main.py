import itertools


def culculate(arr_cul, P_cul, Q_cul):
    a = arr_cul.index(P_cul)
    b = arr_cul.index(Q_cul)

    ans = abs(a - b)
    return ans


if __name__ == '__main__':
    N = int(input())
    P = tuple(map(int, input().split()))
    Q = tuple(map(int, input().split()))

    arr = list(itertools.permutations([x + 1 for x in range(N)]))

    print(culculate(arr, P, Q))
