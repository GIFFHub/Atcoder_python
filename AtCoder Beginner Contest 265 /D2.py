import itertools


def judge(n, a_cum):
    return 1


if __name__ == '__main__':
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))

    A_cum = list(itertools.accumulate(A))
    print(judge(N, A_cum))
