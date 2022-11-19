import sys
sys.setrecursionlimit(200000)


def trans(i):
    if not know[i-1]:
        know[i-1] = True
        return trans(A[i-1])
    else:
        return


if __name__ == '__main__':
    N, X = map(int, input().split())
    A = list(map(int, input().split()))

    know = [False]*N

    trans(X)

    print(know.count(True))
