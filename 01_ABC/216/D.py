from collections import deque
import sys


def addition_ball(x, target):
    if x not in s:
        s.add(x)
        d[x] = target
    # すでに集めている先頭郡の中に、今回持ってきた色がある場合
    elif x in s:
        s.remove(x)
        target_cy = d.pop(x)
        if len(A[target_cy]) > 0:
            y = A[target_cy].popleft()
            addition_ball(y, target_cy)
        if len(A[target]) > 0:
            z = A[target].popleft()
            addition_ball(z, target)
    return


if __name__ == '__main__':
    sys.setrecursionlimit(5000000)
    N, M = map(int, input().split())
    A = [[] for _ in range(M)]
    for i in range(M):
        k = int(input())
        A[i] = deque(list(map(int, input().split())))

    tops = []
    s = set()
    d = dict()
    for i in range(M):
        # まず各シリンダの先頭を集める
        add_ball0 = A[i].popleft()
        addition_ball(add_ball0, i)

    for i in range(M):
        if len(A[i]) > 0:
            print('No')
            break
    else:
        print('Yes')

