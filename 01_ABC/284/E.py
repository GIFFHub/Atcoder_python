from collections import deque

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

    M = 10**6
    dq = deque()
    dq.append(1)
    visit = set()
    ans = 1
    while len(dq) > 0:
        current_p = dq.popleft()
        visit.add(current_p)
        if current_p in d:
            for next_p in d[current_p]:
                if next_p not in visit:
                    visit.add(next_p)
                    ans += 1
                    dq.append(next_p)
                    if ans > M:
                        print(M)
                        exit()

    print(ans)






