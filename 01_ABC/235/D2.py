from collections import deque

if __name__ == '__main__':
    a, N = map(int, input().split())

    M = 1
    while M <= N:
        M *= 10
    d = [-1] * M
    Q = deque()
    d[1] = 0
    Q.append(1)

    while len(Q):
        c = Q.popleft()
        dc = d[c]

        op1 = a * c
        # 乗算
        if op1 < M and d[op1] == -1:
            d[op1] = dc + 1
            Q.append(op1)

        # 入れ替え
        if c >= 10 and c % 10 != 0:
            s = str(c)
            op2 = int(s[-1] + s[:-1])
            if op2 < M and d[op2] == -1:
                d[op2] = dc + 1
                Q.append(op2)
    print(d[N])