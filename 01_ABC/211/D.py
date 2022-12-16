from collections import deque
import sys
sys.setrecursionlimit(5000000)


def trace(pos, path):
    global ans
    if pos == 0:
        ans += 1
        ans %= C
        return
    if path < 1:
        return

    for p in T[pos]:
        if dist[p] == path-1:
            trace(p, path-1)
    return


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = []
    B = []
    T = [deque() for _ in range(N)]
    C = 10**9+7
    for _ in range(M):
        a, b = map(int, input().split())
        T[a-1].append(b-1)
        T[b-1].append(a-1)

    d = deque()
    d.append(0)

    dist = dict()
    dist[0] = 0

    while True:
        if len(d) > 0:
            current_city = d.popleft()
            for i in T[current_city]:
                if i not in dist:
                    dist[i] = dist[current_city]+1
                    d.append(i)
        else:
            break

    if N-1 not in dist:
        print(0)
    else:
        min_path = dist[N-1]

        tmp = N-1
        ans = 0
        trace(N-1, dist[N-1])

        print(ans)


