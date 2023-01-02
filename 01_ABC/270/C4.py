from collections import deque
import sys

sys.setrecursionlimit(5000000)


def dfs(p):
    global ans
    if p == Y:
        ans.append(p)
        print(*ans)
        return ans
    else:
        past.add(p)
        ans.append(p)
        for n in d[p]:
            if n not in past:
                dfs(n)
        ans.pop()
        return ans


if __name__ == '__main__':
    N, X, Y = map(int, input().split())
    d = dict()
    ans = deque()
    for _ in range(N-1):
        u, v = map(int, input().split())
        if u in d:
            d[u].append(v)
        else:
            d[u] = [v]
        if v in d:
            d[v].append(u)
        else:
            d[v] = [u]

    past = set()
    #dfs(X)

    ans = dfs(X)
    print(*ans)




