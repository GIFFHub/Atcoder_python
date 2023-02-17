
from collections import deque

if __name__ == '__main__':
    N, M = map(int, input().split())
    d = dict()
    for _ in range(M):
        a, b = map(int, input().split())
        if a in d:
            d[a].append(b)
        else:
            d[a] = [b]
        if b in d:
            d[b].append(a)
        else:
            d[b] = [a]

    landmark = dict()
    visit = [False]*N
    dq = deque()
    dq.append(1)
    visit[0] = True
    while dq:
        now = dq.popleft()
        nxts = d[now]

        for n in nxts:
            if not visit[n-1]:
                dq.append(n)
                landmark[n] = now
                visit[n-1] = True

    print('Yes')
    for i in range(2, N+1):
        print(landmark[i])




