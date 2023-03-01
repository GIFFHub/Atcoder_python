from collections import deque

if __name__ == '__main__':
    S = deque(input())
    Q = int(input())

    flg = 0
    for _ in range(Q):
        query = list(input().split())
        T = query[0]
        if T == '1':
            flg = 1 - flg
        else:
            F = query[1]
            C = query[2]
            if flg:
                if F == '1':
                    S.append(C)
                else:
                    S.appendleft(C)
            else:
                if F == '1':
                    S.appendleft(C)
                else:
                    S.append(C)
    if flg:
        S.reverse()
    print(''.join(S))

