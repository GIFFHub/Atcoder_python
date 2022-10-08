from collections import deque

if __name__ == '__main__':
    N, M = map(int, input().split())
    table = [[-1] * N for _ in range(N)]
    table[0][0] = 0
    Q1 = deque()
    Q2 = deque()
    Q1.append((1, 1))
    num = 1
    tmp = 0
    while len(Q1) >= 1:
        (i, j) = Q1.popleft()
        for k in range(1, N + 1):
            for l in range(1, N + 1):
                if ((i - k) ** 2 + (j - l) ** 2) == M and table[k - 1][l - 1] == -1:
                    table[k - 1][l - 1] = num
                    Q2.append((k, l))
        if len(Q1) == 0:
            Q1 = Q2
            Q2 = deque()
            num += 1

    for n in range(N):
        for m in range(N):
            if m == 0:
                print('%d' % table[n][m], end='')
            else:
                print(' %d' % table[n][m], end='')
        print()
