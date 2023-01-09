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

    past = set()
    ans = 0
    dq = deque()
    for i in range(1, N+1):
        if i not in past:
            ans += 1
            dq.append(i)
            while len(dq) > 0:
                p = dq.popleft()
                past.add(p)
                if p in d:
                    for t in d[p]:
                        if t not in past:
                            dq.append(t)
                            #past.add(t)

    print(ans)




