from collections import deque
import sys

sys.setrecursionlimit(50000000)


def visit(current_p):
    global ans
    global past
    global tmp_past
    past.add(current_p)
    if current_p in d:
        for next_p in d[current_p]:
            if next_p not in past:
                ans += 1
                if ans > M:
                    print(M)
                    exit()
                visit(next_p)
                past.discard(next_p)


if __name__ == '__main__':
    N, M = map(int, input().split())
    d = dict()
    for _ in range(M):
        u, v = map(int, input().split())
        if u not in d:
            d[u] = [v]
        else:
            d[u].append(v)

        if v not in d:
            d[v] = [u]
        else:
            d[v].append(u)

    ans = 1
    M = 10**6
    past = set()
    tmp_past = set()
    visit(1)
    print(ans)






