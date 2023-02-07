import sys
sys.setrecursionlimit(500000000)


def check(current_pos, prev_pos):
    global ans
    # 行ったことある場合
    if visit[current_pos-1]:
        return
    else:
        visit[current_pos-1] = True
        # それぞれの次の点について
        if current_pos in d:
            for nxt in d[current_pos]:
                # 行ったことがなければ
                if not visit[nxt-1]:
                    check(nxt, current_pos)
                # 行ったことがあれば
                else:
                    if nxt != prev_pos:
                        ans += 1


if __name__ == '__main__':
    N, M = map(int, input().split())
    d = dict()
    ans = 0
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

    visit = [False] * N

    for i in range(1, N):
        check(i, 0)

    print(ans//2)

