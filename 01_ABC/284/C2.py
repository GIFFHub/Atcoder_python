from collections import deque
import sys

sys.setrecursionlimit(5000000)


def visit(p):
    past.add(p)
    if p in d:
        for t in d[p]:
            if t not in past:
                visit(t)


if __name__ == '__main__':
    N, M = map(int, input().split())
    d = dict()

    for _ in range(M):
        u, v = map(int, input().split())
        if u in d:
            d[u].append(v)
        else:
            d[u] = deque([v])
        if v in d:
            d[v].append(u)
        else:
            d[v] = deque([u])

    past = set()
    ans = 0
    for i in range(1, N+1):
        if i not in past:
            ans += 1
            visit(i)

    print(ans)










