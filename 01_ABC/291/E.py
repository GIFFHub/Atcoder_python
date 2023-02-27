
from collections import deque
import sys
sys.setrecursionlimit(50000000)


def check(current, cnt):
    global ans
    global visit
    visit[current-1] = True
    # 次の行き先がある場合
    if current in nxts:
        for nxt in nxts[current]:
            if visit[nxt-1]:
                continue
            ans.append(nxt)
            check(nxt, cnt+1)
            visit[nxt-1] = False

    else:
        if cnt == N:
            T = [0]*N
            for i in range(N):
                T[ans[i]-1] = i+1
            print('Yes')
            print(*T)
            exit()
        else:
            ans.pop()
            visit[current-1] = False
            return


if __name__ == '__main__':
    N, M = map(int, input().split())
    nxts = dict()
    back_nxts = dict()
    ans = deque()
    visit = [False]*N
    for _ in range(M):
        x, y = map(int, input().split())
        if x in nxts:
            nxts[x].append(y)
        else:
            nxts[x] = [y]
        if y in back_nxts:
            back_nxts[y].append(x)
        else:
            back_nxts[y] = [x]

    start_point = 0

    for i in range(1, N+1):
        if i not in back_nxts:
            start_point = i
            break
    else:
        print('No')
        exit()
    visit[start_point-1] = True
    ans.append(start_point)
    check(start_point, 1)
    print('No')

