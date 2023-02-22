

if __name__ == '__main__':
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    nxt = []
    visit = [False]*N
    now = 0
    while not visit[now]:
        visit[now] = True
        nxt.append(now)
        now = A[now]-1

    # ループの始まり
    start = nxt.index(now)

    non_loop = nxt[:start]
    loop = nxt[start:]

    len_non_loop = len(non_loop)
    len_loop = len(loop)
    # ループ開始前に目的地までたどり着く場合
    if K+1 < len_non_loop:
        ans = non_loop[K]+1
    else:
        # 全てのループが終わったあと、移動する回数
        last_move = (K - len_non_loop) % len_loop
        ans = loop[last_move]+1

    print(ans)



