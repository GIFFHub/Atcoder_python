
from collections import deque
from collections import defaultdict
import sys
sys.setrecursionlimit(50000000)
#import pypyjit
#pypyjit.set_param('max_unroll_recursion=-1')


def check(current):
    global ans
    global d
    nxt_pos = 0
    # 次の行き先がある場合
    if current in nxts:
        for nxt in nxts[current]:
            d[nxt] -= 1
            if d[nxt] == 0:
                nxt_pos = nxt
    if not nxt_pos == 0:
        ans.append(nxt_pos)
        check(nxt_pos)
    else:
        if len(ans) == N:
            T = [0]*N
            for i in range(N):
                T[ans[i]-1] = i+1
            print('Yes')
            print(*T)
            exit()
        else:
            print('No')
            exit()


if __name__ == '__main__':
    N, M = map(int, input().split())
    nxts = dict()
    ans = deque()
    past = dict()
    K = range(1, N+1)
    s_K = set(K)
    # 各頂点に入る辺の数
    d = defaultdict(int)
    for _ in range(M):
        x, y = map(int, input().split())
        if x in nxts:
            nxts[x].append(y)
        else:
            nxts[x] = [y]
        d[y] += 1
        if y in s_K:
            s_K.remove(y)

    start_point = 0
    len_s_K = len(s_K)
    if len_s_K != 1:
        print('No')
        exit()
    start_point = list(s_K)[0]
    '''
    for i in range(1, N+1):
        if i not in d:
            start_point = i
            break
    else:
        print('No')
        exit()
    '''
    ans.append(start_point)
    check(start_point)

