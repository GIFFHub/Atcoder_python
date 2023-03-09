from collections import deque

if __name__ == '__main__':
    H, W = map(int, input().split())
    S = []
    d = dict()
    for _ in range(H):
        S.append(input())

    for i in range(H*W):
        h = i // W
        w = i % W
        # 下
        if h+1 < H:
            if S[h+1][w] == '.':
                if i in d:
                    d[i].append(i+W)
                else:
                    d[i] = [i+W]
        # 上
        if h-1 >= 0:
            if S[h-1][w] == '.':
                if i in d:
                    d[i].append(i-W)
                else:
                    d[i] = [i-W]
        # 右
        if w+1 < W:
            if S[h][w+1] == '.':
                if i in d:
                    d[i].append(i+1)
                else:
                    d[i] = [i+1]

        # 左
        if w-1 >= 0:
            if S[h][w-1] == '.':
                if i in d:
                    d[i].append(i-1)
                else:
                    d[i] = [i-1]

    ans = 0
    for i in range(H*W):
        h = i // W
        w = i % W
        if S[h][w] == '#':
            continue
        dq = deque()
        dist = [H*W+1] * (H*W)
        dist[i] = 0
        visit = [False] * (H*W)
        visit[i] = True
        dq.append(i)
        cnt = 0
        while dq:
            current_pos = dq.popleft()
            if current_pos in d:
                nxts = d[current_pos]
                for nxt in nxts:
                    dist[nxt] = min(dist[nxt], dist[current_pos]+1)
                    if not visit[nxt]:
                        dq.append(nxt)
                        visit[nxt] = True
        for i in range(H*W):
            if dist[i] == H*W+1:
                dist[i] = -1

        ans = max(ans, max(dist))

    print(ans)



