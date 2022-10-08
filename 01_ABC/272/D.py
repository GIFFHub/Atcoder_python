import sys


def check_move(num, i, j):
    for k in range(1, N+1):
        for l in range(1, N+1):
            if ((i - k) ** 2 + (j - l) ** 2) == M and table[k-1][l-1] > num:
                table[k-1][l-1] = num
                check_move(num + 1, k, l)


if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    N, M = map(int, input().split())
    table = [[10 ** 5] * N for _ in range(N)]
    table[0][0] = 0
    check_move(1, 1, 1)
    for n in range(N):
        for m in range(N):
            if table[n][m] == 10**5:
                table[n][m] = -1

    for n in range(N):
        for m in range(N):
            if m == 0:
                print('%d' % table[n][m], end='')
            else:
                print(' %d' % table[n][m], end='')
        print()
