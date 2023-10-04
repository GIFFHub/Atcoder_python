from collections import deque

if __name__ == '__main__':
    H, W = map(int, input().split())
    S = []
    for _ in range(H):
        S.append(input())

    d = dict()
    d['s'] = 'n'
    d['n'] = 'u'
    d['u'] = 'k'
    d['k'] = 'e'
    d['e'] = 's'

    dq = deque()
    if S[0][0] != 's':
        print('No')
        exit()
    dq.append((0, 0))

    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    s = set()
    while len(dq) >= 1:
        pos = dq.popleft()
        if pos in s:
            continue
        else:
            s.add(pos)
        nxt_s = d[S[pos[0]][pos[1]]]

        for dir in direction:
            nxt_pos = (pos[0]+dir[0], pos[1]+dir[1])
            if nxt_pos[0] < 0:
                continue
            if nxt_pos[0] >= H:
                continue
            if nxt_pos[1] < 0:
                continue
            if nxt_pos[1] >= W:
                continue

            if S[nxt_pos[0]][nxt_pos[1]] == nxt_s:
                if nxt_pos == (H-1, W-1):
                    print('Yes')
                    exit()
                else:
                    if S[nxt_pos[0]][nxt_pos[1]] in d:
                        dq.append(nxt_pos)
    print('No')












