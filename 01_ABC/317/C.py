

def dfs(current_point, tmp_dist):
    global ans
    global dist

    dist += tmp_dist
    if current_point in d:
        nxts = d[current_point]
        for nxt in nxts:
            if not past[nxt[0]]:
                past[nxt[0]] = True
                dfs(nxt[0], nxt[1])

        past[current_point] = False
        ans = max(ans, dist)
        dist -= tmp_dist
    return


if __name__ == '__main__':
    N, M = map(int, input().split())
    d = dict()
    for _ in range(M):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        if a in d:
            d[a].append((b, c))
        else:
            d[a] = [(b, c)]
        if b in d:
            d[b].append((a, c))
        else:
            d[b] = [(a, c)]

    ans = 0
    dist = 0
    # スタート遅延で全探索
    for i in range(N):
        past = [False] * N
        past[i] = True
        dfs(i, 0)

    print(ans)







