from collections import deque

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

    past = [0] * (N+1)
    ans = 0
    dq = deque()
    for i in range(1, N+1):
        if not past[i]:
            ans += 1
            dq.append(i)
            while len(dq) > 0:
                p = dq.popleft()
                past[p] = 1
                if p in d:
                    for t in d[p]:
                        if not past[t]:
                            dq.append(t)

    print(ans)




