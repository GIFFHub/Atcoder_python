from collections import deque

if __name__ == '__main__':
    a, N = map(int, input().split())
    M = 10**6
    d = dict()
    d[1] = 0
    T = deque([1])
    while len(T) > 0:
        t = T.popleft()

        op1 = t * a
        if op1 not in d:
            if op1 < M:
                d[op1] = d[t] + 1
                T.append(op1)
        if t > 10:
            if str(t)[-1] != '0':
                op2 = int(str(t)[-1] + str(t)[:-1])
                if op2 not in d:
                    if op2 < M:
                        d[op2] = d[t] + 1
                        T.append(op2)
    if N in d:
        print(d[N])
    else:
        print(-1)



