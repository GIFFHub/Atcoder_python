
from collections import deque
import sys
sys.setrecursionlimit(5000000)


def make_sequence(pre, cnt):
    global A
    global ans
    if cnt == N:
        tmp = 0
        for t in T:
            if A[t[1]-1]-A[t[0]-1] == t[2]:
                tmp += t[3]
        ans = max(ans, tmp)
        return
    for x in range(pre, M+1):
        A.append(x)
        make_sequence(x, cnt+1)
        A.pop()


if __name__ == '__main__':

    N, M, Q = map(int, input().split())
    T = []
    for _ in range(Q):
        a, b, c, d = map(int, input().split())
        T.append((a, b, c, d))

    A = deque()
    ans = 0
    cnt = 0
    make_sequence(1, 0)
    print(ans)