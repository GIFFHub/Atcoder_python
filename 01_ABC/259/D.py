import math
from collections import deque

def cal_distance(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2


def check_overlap(cir1, cir2):
    dist = cal_distance((cir1[0], cir1[1]), (cir2[0], cir2[1]))
    if (cir1[2]-cir2[2])**2 <= dist <= (cir1[2]+cir2[2])**2:
        return True
    else:
        return False


if __name__ == '__main__':
    N = int(input())
    sx, sy, tx, ty = map(int, input().split())
    s = (sx, sy)
    t = (tx, ty)
    start = -1
    goal = -1
    cir = []
    d = dict()
    for i in range(N):
        x, y, r = map(int, input().split())
        cir.append((x, y, r))

        if (sx-x)**2 + (sy-y)**2 == r**2:
            start = i
        if (tx-x)**2 + (ty-y)**2 == r**2:
            goal = i

    for i in range(N):
        for j in range(i+1, N):
            if check_overlap(cir[i], cir[j]):
                if i in d:
                    d[i].append(j)
                else:
                    d[i] = [j]
                if j in d:
                    d[j].append(i)
                else:
                    d[j] = [i]

    past = set()
    past.add(start)
    dq = deque([start])
    if start not in d:
        if start == goal:
            print('Yes')
        else:
            print('No')
    else:
        while len(dq) > 0:
            next_cir = dq.popleft()
            for ds in d[next_cir]:
                if ds not in past:
                    dq.append(ds)
                    past.add(ds)

        if goal in past:
            print('Yes')
        else:
            print('No')








