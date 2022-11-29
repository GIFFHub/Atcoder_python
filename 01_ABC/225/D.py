import sys
sys.setrecursionlimit(10000000)
from collections import deque

def checkfront(x):
    if x not in d_front:
        return x

    if d_front[x] is None:
        return x

    return checkfront(d_front[x])


def setans(x):
    global ans
    if x not in d_back:
        ans.append(x)
        return

    if d_back[x] is None:
        ans.append(x)
        return

    ans.append(x)
    return setans(d_back[x])


if __name__ == '__main__':
    N, Q = map(int, input().split())
    d_front = dict()
    d_back = dict()
    for _ in range(Q):
        query = list(map(int, input().split()))

        if query[0] == 1:
            d_back[query[1]] = query[2]
            d_front[query[2]] = query[1]

        elif query[0] == 2:
            d_back[query[1]] = None
            d_front[query[2]] = None

        elif query[0] == 3:
            ans = deque()
            front = checkfront(query[1])
            setans(front)
            ans.appendleft(len(ans))
            print(*ans)

