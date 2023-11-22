from collections import deque

if __name__ == '__main__':
    S = input()
    dq = deque()
    for s in S:
        dq.append(s)
        if len(dq) >= 3:
            if dq[-3]+dq[-2]+dq[-1] == 'ABC':
                dq.pop()
                dq.pop()
                dq.pop()
    for d in dq:
        print(d, end='')


