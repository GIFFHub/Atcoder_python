
from collections import deque
from collections import defaultdict

if __name__ == '__main__':
    N, M = map(int, input().split())
    d = dict()
    num = [0]*N
    for _ in range(M):
        u, v = map(int, input().split())
        if u in d:
            d[u].add(v)
        else:
            d[u] = set()
            d[u].add(v)
        num[u-1] += 1
    cnt = [0]*N
    for i in range(1, N+1):
        dq = deque()
        dq.append(i)
        visit = [False]*N
        visit[i-1] = True
        while dq:
            current_pos = dq.pop()
            # 現在の点から有向辺がある場合
            if current_pos in d:
                for next_pos in d[current_pos]:
                    if not visit[next_pos-1]:
                        dq.append(next_pos)
                        visit[next_pos-1] = True
                        cnt[i-1] += 1


    ans = 0
    for i in range(N):
        ans += cnt[i]-num[i]

    print(ans)



