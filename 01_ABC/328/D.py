from collections import deque

if __name__ == '__main__':
    S = input()
    dq = deque()
    for s in S:
        if len(dq) == 0:
            dq.append(s)
            continue
        if s == 'A':
            dq.append('A')
        elif s == 'B':
            if dq[-1] == 'A':
                dq.pop()
                dq.append('AB')
            else:
                dq.append('B')
        elif s == 'C':
            if dq[-1] == 'AB':
                dq.pop()
            else:
                dq.append('C')

    for d in dq:
        print(d, end='')


